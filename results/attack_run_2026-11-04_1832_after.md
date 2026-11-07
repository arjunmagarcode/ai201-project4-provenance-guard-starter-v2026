# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:32
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "af63dfec-5af9-4610-a42f-866d67598a89",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3365,
  "model_score": 0.1635,
  "style_score": 0.5095,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "44196295-4a19-42d3-956d-d564359d77ba",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3925,
  "model_score": 0.5943,
  "style_score": 0.1906,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c8c5c7b7-b611-497b-82ec-39880d2f5540",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5158,
  "model_score": 0.6662,
  "style_score": 0.3654,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b76d0b3a-038a-4d7c-a93e-5e6d08d4331c",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5558,
  "model_score": 0.6114,
  "style_score": 0.5003,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e01eab90-c95d-412a-9774-1793a352b38c",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2791,
  "model_score": 0.3212,
  "style_score": 0.237,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "836d8df3-c317-496b-a903-64812381e8ce",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3825,
  "model_score": 0.5727,
  "style_score": 0.1922,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "dc47120e-4e13-4172-96d8-72b4ca46548e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5686,
  "model_score": 0.5862,
  "style_score": 0.551,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "ddec6658-7166-4e4b-a602-f602d15de94e",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3519,
  "model_score": 0.2452,
  "style_score": 0.4586,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "4b653001-5233-4d53-8e52-a215eee18a53",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.529,
  "model_score": 0.7042,
  "style_score": 0.3538,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "e8bf24fe-7efd-461e-8fe8-e0d890592e5e",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8629,
  "model_score": 0.9792,
  "style_score": 0.7466,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "931ba76d-ea87-48f6-842e-731ea919f4fc",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5077,
  "model_score": 0.6175,
  "style_score": 0.3979,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7babd040-92c3-4cac-bb87-c49683b53bad",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6233,
  "model_score": 0.7387,
  "style_score": 0.5079,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "66a5c62e-f177-4003-a272-5cf91eb612bc",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6314,
  "model_score": 0.8051,
  "style_score": 0.4576,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "1a0b3806-3b65-4835-8498-28d26b1a352f",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6229,
  "model_score": 0.8329,
  "style_score": 0.4129,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "1038d7f5-5cad-452d-939e-740dc5700c72",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6925,
  "model_score": 0.8005,
  "style_score": 0.5845,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "bfc164fd-4227-4cfd-9365-45b0e65cb491",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6148,
  "model_score": 0.8814,
  "style_score": 0.3482,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "8fa15383-cae2-4063-bbcc-6a59b7763300",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6701,
  "model_score": 0.8816,
  "style_score": 0.4585,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "5de8cf74-1521-4fac-8911-bdc98ae21dbe",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3529,
  "model_score": 0.3223,
  "style_score": 0.3835,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f551f2d9-f4cc-43b7-989f-023083952cfc",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3656,
  "model_score": 0.4625,
  "style_score": 0.2687,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "e4253305-b706-4331-b2ad-3803e0ea0911",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.234,
  "model_score": 0.2044,
  "style_score": 0.2637,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "922b6075-a1a4-4fbd-b1b2-1b431846e479",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5048,
  "model_score": 0.5943,
  "style_score": 0.4152,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "5b557dae-4718-4e02-8848-0fd48a016183",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4386,
  "model_score": 0.4998,
  "style_score": 0.3774,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "eb5b850d-e9ab-4a31-a0d1-7b811c506059",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4787,
  "model_score": 0.6401,
  "style_score": 0.3173,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "3064d943-e383-4494-91a5-102d7edf086c",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4818,
  "model_score": 0.5583,
  "style_score": 0.4053,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "29f4bed6-46ea-49a4-a182-1a4530e3b724",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3,
  "model_score": 0.0,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "fcb5ff3d-1b55-4875-9272-f0317d23909b",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4056,
  "model_score": 0.0112,
  "style_score": 0.8,
  "label": "We cannot tell reliably whether this was written by a person or an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4885ccec-92ff-4afb-86f7-c08df053f337",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7988,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "7387eeab-f194-47dd-9bb7-450918b10db6",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "b8d1255c-ca40-4952-9505-b6580bc99479",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably written by an AI system.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1357b088-5a2e-4482-8105-66bc0ccd81e5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "cd8bb4ca-00a0-4b85-8d76-9459733a8c59",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "5a0f12d6-542a-476c-921d-ed0a121e9aca",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "2421a7d9-b090-423d-9239-49430bc467a3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c2c3a7a9-efea-4cf9-9419-ddc30d97f221",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "81c0ad72-9a98-426b-934e-2939cb406200",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "ae354a0d-b6c7-4d63-ba60-b1e74bfca4e9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "880072b6-1a72-4781-9701-de63f9e6d905",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "b412262a-bdb6-4525-b95a-0e5583d1043e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "a301dac3-09bf-4a33-9464-da74c1c574e8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
