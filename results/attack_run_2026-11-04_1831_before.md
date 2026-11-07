# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 18:31
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
  "content_id": "afa74c6b-c37a-4aff-b547-c1308bf0a373",
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
  "content_id": "ca40aef1-97a0-431b-9b24-39f3579b826d",
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
  "content_id": "be7f8193-42da-417a-ac32-c74e004ec477",
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
  "content_id": "909042b9-0893-4ef2-a79b-45d515717825",
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
  "content_id": "477a04fc-1342-41c6-9fca-1ed2d7403e03",
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
  "content_id": "5ec4d428-e9ef-4545-b2c8-e6acd79e6446",
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
  "content_id": "30e3875d-c00f-46fc-8790-f55c663d9c3e",
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
  "content_id": "eaa6f14b-51cc-4e97-b614-468eaae36565",
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
  "content_id": "e310bf29-5c15-48db-83ff-040ce830d5ef",
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
  "content_id": "8d3add2a-2d32-4931-af9a-369cf65e1f90",
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
  "content_id": "b38f3aaf-fe83-46fe-9b9e-61b5f74a11ea",
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
  "content_id": "67cd0346-f6e9-4c79-acf8-265b076537e0",
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
  "content_id": "69e7a8bd-72f5-4281-81f7-a6c507a9265d",
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
  "content_id": "a9cb552a-ee0b-4732-8334-b1d8618e4952",
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
  "content_id": "dedda10b-e791-4477-9197-c1b0671bc040",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6925,
  "model_score": 0.8005,
  "style_score": 0.5845,
  "label": "We think this was probably written by an AI system.",
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
  "content_id": "3c60ad85-ff64-4f12-8374-e573f0e857ec",
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
  "content_id": "928bdfee-31f9-438c-8a66-2aa14f22d497",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6701,
  "model_score": 0.8816,
  "style_score": 0.4585,
  "label": "We think this was probably written by an AI system.",
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
  "content_id": "aec965e2-d233-4993-a6c2-3b1097117b2a",
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
  "content_id": "414adef7-fa63-47d7-ac30-5ea6095280d1",
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
  "content_id": "c182ea71-a88e-43ab-a18f-a1fedd2e84ad",
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
  "content_id": "9839deee-e03d-4b4d-bff2-b62e620eec60",
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
  "content_id": "9e955ccb-1f56-41cd-b6ff-25531fd10095",
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
  "content_id": "a7a07b4b-4936-40c4-8e4d-13a40c8eb744",
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
  "content_id": "80b14bb8-ed42-4268-8832-9d79f2dbf51f",
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
  "content_id": "8fdcf62a-c442-4e35-9906-d138140153c8",
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
  "content_id": "1fec256c-e893-473a-9b56-57a305e36d35",
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
  "content_id": "75227fa0-3a19-4c4e-b44b-57d7261066d9",
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
  "content_id": "7fb09ae3-798b-4e98-a258-ad43e855ec96",
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
  "content_id": "db264417-30f4-4e74-9383-ebb9e522856c",
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
  "content_id": "badc9bf6-7766-4eb7-b118-35dce8e66263",
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
  "content_id": "3958473c-743b-42c8-93f8-685c3e5970cf",
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
  "content_id": "6b0fb399-0fa4-404d-bf72-40f7e61fe715",
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
  "content_id": "a15d48ca-f794-47ad-9a48-3e01915584f4",
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
  "content_id": "09bccb05-b327-4223-9362-85b1a743e599",
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
  "content_id": "b3ca849f-08f1-40a7-a99b-3f14391da4dc",
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
  "content_id": "5651a8cd-3a29-4042-9b60-867b1f89152f",
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
  "content_id": "69496c3d-9bbf-433a-b13a-81dc3c2b7349",
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
  "content_id": "fe70e740-c383-4e4f-85cb-f823fc64a3be",
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
  "content_id": "9e8ebb58-0c2b-4b8b-a083-01c7b463ba71",
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
