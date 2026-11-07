# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. `POST /submit` validates a JSON object containing non-empty `text` and
   `creator_id`; text longer than 20,000 characters is rejected.
2. `detector.py::model_signal` measures how predictable the text is to local
   GPT-2; higher scores are more AI-like.
3. `stylometry.py::style_signal` measures sentence-length variation,
   vocabulary variety, and punctuation density; higher scores are more
   AI-like.
4. `scoring.py::combine_signals` calculates a balanced weighted average.
5. `scoring.py::score_to_label` maps the score to `human`, `unsure`, or `ai`.
6. `audit.py::log_decision` records the scores and decision in
   `logs/audit.jsonl`, and the route returns the same evidence as JSON.
7. A writer can submit the returned `content_id` to `POST /appeal`; the appeal
   is appended to the log and changes the item's status to `under_review`.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** GPT-2 perplexity, converted to a 0–1 predictability
score. Lower perplexity means the model found the text easier to predict, so
the returned AI-likelihood score is higher.

**Why that might differ between human and AI writing:** Generated writing
often uses likely next words and familiar sentence patterns, which a language
model can predict easily.

**What it can't see:** Predictability is not authorship. Plain writing by a
second-language writer, younger writer, or careful human can look AI-like, and
unusual human prose can look less AI-like.

### Signal two — the style signal

**What it measures:** Sentence-length spread, type-token ratio (unique words
divided by total words), and punctuation density.

**Why that might differ between human and AI writing:** Generated prose often
has consistent sentence lengths and repeated vocabulary, while human writing
can be more uneven.

**What it can't see:** It cannot understand meaning or authorship. Typos,
quotations, sentence splitting, or other formatting changes can alter the
score without changing who wrote the text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Use a weighted average. When the signals disagree, the result
stays between them and becomes less certain rather than allowing either signal
to decide alone.

**The numbers:** 50% model signal and 50% style signal. Before the
improvement, human was `<= 0.35`, unsure was `0.35–0.65`, and AI was
`>= 0.65`. After the measured improvement, AI is `>= 0.75` and the unsure
band is `0.35–0.75`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** A text
with predictable wording but varied sentence lengths can produce a high model
score and a lower style score. The equal weighting moves the combined score
toward the middle, where the service can say it is unsure instead of making a
high-confidence accusation.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | We think this was probably written by a person. |
| unsure | 0.35–0.75 | We cannot tell reliably whether this was written by a person or an AI system. |
| high-confidence AI | 0.75–1.00 | We think this was probably written by an AI system. |

**Why I worded the "unsure" one this way:** It communicates uncertainty without
calling the writer dishonest. The score is evidence for review, not proof of
who wrote the text.
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json
{
  "confidence": 0.2003,
  "content_id": "c144ed30-78c6-4d4d-90bd-b14d0716b357",
  "guess": "human",
  "label": "We think this was probably written by a person.",
  "model_score": 0.1402,
  "style_score": 0.2604
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json
{
  "content_id": "c144ed30-78c6-4d4d-90bd-b14d0716b357",
  "message": "Your appeal was recorded and is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.2003,
      "content_id": "c144ed30-78c6-4d4d-90bd-b14d0716b357",
      "creator_id": "sample-writer",
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.1402,
      "status": "decided",
      "style_score": 0.2604
    },
    {
      "content_id": "c144ed30-78c6-4d4d-90bd-b14d0716b357",
      "creator_id": "sample-writer",
      "event": "appeal",
      "reasoning": "This sample was written by me for the project test.",
      "status": "under_review"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked AI to read the starter repository and explain the
  service architecture, unfinished milestones, and required endpoint behavior.
- *What came back:* It identified the local model signal, the stylometry signal,
  the scoring pipeline, audit logging, and the appeal workflow.
- *What I changed:* I used that explanation to understand the request flow and
  decide the validation, scoring, and label behavior before implementing it.

**Moment 2**

- *What I asked for:* I asked AI to implement and validate the submission and
  appeal routes, stylometry calculations, scoring, labels, and audit behavior.
- *What came back:* It produced an implementation with input validation,
  append-only logging, two combined signals, three labels, and a tested appeal
  path.
- *What I changed:* I reviewed the implementation, chose a 20,000-character
  input limit and balanced signal weights, ran the supported Python 3.13
  checks, and verified a real local-model submission.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 submissions per minute and 200 per day.

Ten per minute allows normal retries while limiting rapid threshold probing. Two hundred per day allows ordinary use but makes automated mapping expensive. The limiter counts by `creator_id`, falling back to the remote address when no usable creator id is present.

The recorded flood test produced 10 accepted requests followed by 5 rejected requests:

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Evidence: `results/flood_2026-11-04_1831.md`. `GET /health` reported `rate_limiting: true`.

## Attack Run — Before

The complete attack set ran before the improvement: 56 inputs, 0 crashes, and 0 5xx responses. Each input is marked `HELD` when the service resisted the stated attack and `BROKE` when it achieved its target.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `afa74c6b-c37a-4aff-b547-c1308bf0a373` | human | 0.337 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ca40aef1-97a0-431b-9b24-39f3579b826d` | unsure | 0.393 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `be7f8193-42da-417a-ac32-c74e004ec477` | unsure | 0.516 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `909042b9-0893-4ef2-a79b-45d515717825` | unsure | 0.556 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `477a04fc-1342-41c6-9fca-1ed2d7403e03` | human | 0.279 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `5ec4d428-e9ef-4545-b2c8-e6acd79e6446` | unsure | 0.383 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `30e3875d-c00f-46fc-8790-f55c663d9c3e` | unsure | 0.569 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `eaa6f14b-51cc-4e97-b614-468eaae36565` | unsure | 0.352 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `e310bf29-5c15-48db-83ff-040ce830d5ef` | unsure | 0.529 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8d3add2a-2d32-4931-af9a-369cf65e1f90` | ai | 0.863 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b38f3aaf-fe83-46fe-9b9e-61b5f74a11ea` | unsure | 0.508 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `67cd0346-f6e9-4c79-acf8-265b076537e0` | unsure | 0.623 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `69e7a8bd-72f5-4281-81f7-a6c507a9265d` | unsure | 0.631 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `a9cb552a-ee0b-4732-8334-b1d8618e4952` | unsure | 0.623 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `dedda10b-e791-4477-9197-c1b0671bc040` | ai | 0.693 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `3c60ad85-ff64-4f12-8374-e573f0e857ec` | unsure | 0.615 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `928bdfee-31f9-438c-8a66-2aa14f22d497` | ai | 0.670 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `aec965e2-d233-4993-a6c2-3b1097117b2a` | unsure | 0.353 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `414adef7-fa63-47d7-ac30-5ea6095280d1` | unsure | 0.366 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c182ea71-a88e-43ab-a18f-a1fedd2e84ad` | human | 0.234 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9839deee-e03d-4b4d-bff2-b62e620eec60` | unsure | 0.505 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `9e955ccb-1f56-41cd-b6ff-25531fd10095` | unsure | 0.439 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a7a07b4b-4936-40c4-8e4d-13a40c8eb744` | unsure | 0.479 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `80b14bb8-ed42-4268-8832-9d79f2dbf51f` | unsure | 0.482 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 422 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `8fdcf62a-c442-4e35-9906-d138140153c8` | human | 0.300 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `1fec256c-e893-473a-9b56-57a305e36d35` | unsure | 0.406 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `75227fa0-3a19-4c4e-b44b-57d7261066d9` | ai | 0.799 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `7fb09ae3-798b-4e98-a258-ad43e855ec96` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `db264417-30f4-4e74-9383-ebb9e522856c` | ai | 0.953 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `badc9bf6-7766-4eb7-b118-35dce8e66263` | human | 0.314 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3958473c-743b-42c8-93f8-685c3e5970cf` | human | 0.314 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b0fb399-0fa4-404d-bf72-40f7e61fe715` | human | 0.314 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a15d48ca-f794-47ad-9a48-3e01915584f4` | human | 0.314 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `09bccb05-b327-4223-9362-85b1a743e599` | human | 0.314 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b3ca849f-08f1-40a7-a99b-3f14391da4dc` | human | 0.314 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5651a8cd-3a29-4042-9b60-867b1f89152f` | human | 0.314 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `69496c3d-9bbf-433a-b13a-81dc3c2b7349` | human | 0.314 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fe70e740-c383-4e4f-85cb-f823fc64a3be` | human | 0.314 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9e8ebb58-0c2b-4b8b-a083-01c7b463ba71` | human | 0.314 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

Ten representative audit entries, including rejected requests, are recorded in `logs/audit.jsonl` and extracted in `results/audit_extract_before.json`:

```json
{"content_id":"afa74c6b-c37a-4aff-b547-c1308bf0a373","creator_id":"attacker_EV01","guess":"human","model_score":0.1635,"style_score":0.5095,"combined_score":0.3365,"status":"decided"}
{"content_id":"dedda10b-e791-4477-9197-c1b0671bc040","creator_id":"attacker_FP05","guess":"ai","model_score":0.7254,"style_score":0.6608,"combined_score":0.6931,"status":"decided"}
{"content_id":"928bdfee-31f9-438c-8a66-2aa14f22d497","creator_id":"attacker_FP07","guess":"ai","model_score":0.6822,"style_score":0.6578,"combined_score":0.6700,"status":"decided"}
{"creator_id":"attacker_RQ05","event":"rejected","status":"rejected","reason":"text_required"}
{"creator_id":"unknown","event":"rejected","status":"rejected","reason":"invalid_json"}
{"creator_id":"flood_tester","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
{"creator_id":"flood_tester","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
{"creator_id":"attacker_MF08","event":"rejected","status":"rejected","reason":"text_too_long","max_length":20000}
{"content_id":"414adef7-fa63-47d7-ac30-5ea6095280d1","creator_id":"attacker_PI01","guess":"unsure","model_score":0.1931,"style_score":0.5389,"combined_score":0.3660,"status":"decided"}
{"content_id":"8d3add2a-2d32-4931-af9a-369cf65e1f90","creator_id":"attacker_EV10","guess":"ai","model_score":0.8748,"style_score":0.8516,"combined_score":0.8632,"status":"decided"}
```

**Worst outcome:** FP05 was human technical documentation labeled AI at `0.6931`. The cause was the combining rule: both signals scored formal, predictable prose as machine-like, and the old `0.65` threshold converted that score to an accusation.

## Run Log and Verdicts

The corrected scenarios in `scenarios.py` match the five criteria in `criteria.md`. Each was run three times with `run_eval.py --label complete`; the full JSON output is in `results/run_2026-11-07_1409_complete.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---:|---:|---:|---|
| 1. Human-authored writing false positives | At most 1 of 10 labeled AI | 0/10 | 0/10 | 0/10 | MET |
| 2. Score separation | At least 0.20 between reference scores | 0.04 | 0.04 | 0.04 | MISSED |
| 3. All three labels reachable | 3 of 3 labels | 1/3 | 1/3 | 1/3 | MISSED |
| 4. Appeal changes status and is logged | 2/2 return 200 and `under_review` | 2/2 | 2/2 | 2/2 | MET |
| 5. Bad input returns JSON 400 | 4/4 requests | 4/4 | 4/4 | 4/4 | MET |

**Real output excerpts from `run_eval.py::main`:**

```json
{"scenario":"human-authored writing false positives","trial":1,"guesses":["unsure","unsure","unsure","unsure","unsure","unsure","human","unsure","unsure","unsure"],"statuses":[200,200,200,200,200,200,200,200,200,200]}
{"scenario":"score separation","trial":1,"confidences":[0.6006,0.5636,0.2928],"statuses":[200,200,200]}
{"scenario":"label coverage","trial":1,"guesses":["unsure","unsure","unsure"],"statuses":[200,200,200]}
{"scenario":"appeal changes status","trial":1,"appeal_http_statuses":[200,200],"statuses":["under_review","under_review"]}
{"scenario":"bad input","trial":1,"statuses":[400,400,400,400]}
```

**Diagnoses:** Criterion 2 missed at the combining-rule stage: the two reference inputs produced scores too close together, so the measured separation was below `0.20`. Criterion 3 missed at the label-mapping stage: all three calibration texts landed in the unsure interval `0.35–0.75`, so human and AI were not reached. The before attack run's FP05 and FP07 failures were caused by the signal and combining stages scoring formal/repetitive human writing as AI. EV01 and EV05 bypassed detection because editing and typos changed the style signal toward human. MF03–MF07 were accepted because the route validates type and length but not semantic text quality. Prompt-injection inputs were treated as ordinary content because neither signal models intent. The flood attacks were held by the rate limiter before the route.

## The Improvement

**Change:** raised `AI_THRESHOLD` from `0.65` to `0.75` in `config.py`, and made no other scoring or signal change.

**Reason:** FP05 and FP07 were just above the old threshold. The wider unsure band prevents those borderline results from becoming high-confidence accusations, while accepting that more AI text will remain unsure.

### Attack Run — After

The same 56-input attack set was run again after the single threshold change. The full marked table follows:

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `af63dfec-5af9-4610-a42f-866d67598a89` | human | 0.337 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `44196295-4a19-42d3-956d-d564359d77ba` | unsure | 0.393 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c8c5c7b7-b611-497b-82ec-39880d2f5540` | unsure | 0.516 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b76d0b3a-038a-4d7c-a93e-5e6d08d4331c` | unsure | 0.556 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e01eab90-c95d-412a-9774-1793a352b38c` | human | 0.279 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `836d8df3-c317-496b-a903-64812381e8ce` | unsure | 0.383 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `dc47120e-4e13-4172-96d8-72b4ca46548e` | unsure | 0.569 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `ddec6658-7166-4e4b-a602-f602d15de94e` | unsure | 0.352 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4b653001-5233-4d53-8e52-a215eee18a53` | unsure | 0.529 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e8bf24fe-7efd-461e-8fe8-e0d890592e5e` | ai | 0.863 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `931ba76d-ea87-48f6-842e-731ea919f4fc` | unsure | 0.508 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7babd040-92c3-4cac-bb87-c49683b53bad` | unsure | 0.623 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `66a5c62e-f177-4003-a272-5cf91eb612bc` | unsure | 0.631 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1a0b3806-3b65-4835-8498-28d26b1a352f` | unsure | 0.623 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `1038d7f5-5cad-452d-939e-740dc5700c72` | unsure | 0.693 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `bfc164fd-4227-4cfd-9365-45b0e65cb491` | unsure | 0.615 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `8fa15383-cae2-4063-bbcc-6a59b7763300` | unsure | 0.670 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `5de8cf74-1521-4fac-8911-bdc98ae21dbe` | unsure | 0.353 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f551f2d9-f4cc-43b7-989f-023083952cfc` | unsure | 0.366 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e4253305-b706-4331-b2ad-3803e0ea0911` | human | 0.234 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `922b6075-a1a4-4fbd-b1b2-1b431846e479` | unsure | 0.505 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `5b557dae-4718-4e02-8848-0fd48a016183` | unsure | 0.439 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `eb5b850d-e9ab-4a31-a0d1-7b811c506059` | unsure | 0.479 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `3064d943-e383-4494-91a5-102d7edf086c` | unsure | 0.482 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 422 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `29f4bed6-46ea-49a4-a182-1a4530e3b724` | human | 0.300 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `fcb5ff3d-1b55-4875-9272-f0317d23909b` | unsure | 0.406 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `4885ccec-92ff-4afb-86f7-c08df053f337` | ai | 0.799 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `7387eeab-f194-47dd-9bb7-450918b10db6` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `b8d1255c-ca40-4952-9505-b6580bc99479` | ai | 0.953 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1357b088-5a2e-4482-8105-66bc0ccd81e5` | human | 0.314 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cd8bb4ca-00a0-4b85-8d76-9459733a8c59` | human | 0.314 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a0f12d6-542a-476c-921d-ed0a121e9aca` | human | 0.314 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2421a7d9-b090-423d-9239-49430bc467a3` | human | 0.314 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c2c3a7a9-efea-4cf9-9419-ddc30d97f221` | human | 0.314 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81c0ad72-9a98-426b-934e-2939cb406200` | human | 0.314 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ae354a0d-b6c7-4d63-ba60-b1e74bfca4e9` | human | 0.314 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `880072b6-1a72-4781-9701-de63f9e6d905` | human | 0.314 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b412262a-bdb6-4525-b95a-0e5583d1043e` | human | 0.314 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a301dac3-09bf-4a33-9464-da74c1c574e8` | human | 0.314 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

False positives labeled AI fell from 2 to 0. Overall AI labels fell from 6 to 4, while unsure labels increased from 19 to 21. The improvement helped the false-positive target, but did not solve evasion, prompt-injection, or malformed-content weaknesses.

## What's Still Broken

EV01 and EV05 still evade as human, and EV02–EV09 mostly remain unsure. Prompt-injection inputs are treated as ordinary text because neither signal understands intent. MF03–MF07 are accepted and scored despite control characters, punctuation-only input, emoji, a long token, and right-to-left text. Criterion 2 still misses its separation target, and criterion 3 still cannot reach human or AI using its calibration set. I stopped after one threshold change because the assignment permits one measured improvement; the next fixes should add content-quality validation and a signal less sensitive to surface formatting.

In production I would keep the wider unsure band: fewer false accusations protect real writers, while reviewers pay the cost of handling more borderline cases and some AI text passes to review.


<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [x] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [x] Two signals that measure DIFFERENT things, each with a named blind spot
       [x] Three label variants, all reachable, written out in full
       [x] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [x] Sample Run: a submission AND an appeal, as pasted text
       [x] At least four new commits
       [x] Repository URL submitted:
           https://github.com/arjunmagarcode/ai201-project4-provenance-guard-starter-v2026

     SUBMISSION CHECKLIST — unit 8

       [x] Rate limiting on /submit, with your numbers justified
       [x] The pasted run of status codes showing 429
       [x] Audit log with all nine fields, recording rejections too
       [x] The attack set run IN FULL, every input with an outcome
       [x] Ten audit log entries pasted as text
       [x] Five criteria across three trials
       [x] A diagnosis for every miss and every broken attack — stage AND mechanism
       [x] One improvement, with Attack Run — After
       [x] What's Still Broken, including the production trade
       [x] At least four new commits
       [x] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
