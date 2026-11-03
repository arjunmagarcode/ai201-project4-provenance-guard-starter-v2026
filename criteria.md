# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Of 10 pieces of writing I identify as human-authored, no more than 1 is
labeled high-confidence AI.

**Why this target:**

Accusing a real writer is more harmful than allowing some AI-written text
through, so false positives must be rare.


---

## 2.

Clearly human and clearly AI test texts should have combined scores at least
0.20 apart in each of three evaluation trials.

**Why this target:**

The system needs a measurable separation between its reference cases, while
allowing for variation from the local model.


---

## 3.

At least one test input must produce each of the `human`, `unsure`, and `ai`
labels in the score ranges defined by `config.py`.

**Why this target:**

All three outcomes are part of the service contract. An unreachable label
would make the user-facing uncertainty design incomplete.


---

## 4.

For every valid submission, an appeal with its returned `content_id` must
return HTTP 200, report `under_review`, and add an appeal entry to the audit
log.

**Why this target:**

An appeal is the writer's only immediate response to a disputed decision, so
it must be observable and reliably connected to the original submission.


---

## 5.

Missing, empty, non-string, and over-20,000-character `text` values must
return HTTP 400 with a JSON error, and none may produce an HTTP 500.

**Why this target:**

Malformed input is expected in real traffic and attack traffic. Returning a
clear client error is safer than crashing or creating a fake decision.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
