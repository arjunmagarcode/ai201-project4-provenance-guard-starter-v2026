"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

    "appeals" a list of texts. Each is submitted and then appealed using its
              returned content_id, so the appeal workflow can be tested.
"""

SCENARIOS = [
    {
        "name": "human-authored writing false positives",
        "criterion": 1,
        "texts": [
            "We got to the campsite about four. The pitch was fine, a bit sloped, but there was a tap nearby and the toilets were clean enough. Putting the tent up took longer than it should have because I had forgotten how the poles went. The weather held until Saturday night. Then it rained hard and kept raining. We stayed in the tent and played cards and ate most of the food we had brought for Sunday.",
            "I want to describe my experience of the first month in this country. The weather was very different from my home. I did not expect the rain to continue for so many days. My colleagues were kind and they helped me to find an apartment. I am still learning the words that people use in the office, but each week is a little easier.",
            "I missed the bus this morning because I left my keys on the kitchen table. By the time I noticed, the doors had locked and I had to wait for my roommate to come home. I arrived late, but my manager said it was fine.",
            "The old cupboard does not close properly. I tried tightening the hinge, which helped for a day, but it is loose again now. I will probably replace it when I have enough time to measure the door.",
            "My sister called after dinner and asked about the new job. I told her the work is interesting but the commute is longer than I expected. We talked for ten minutes, then she remembered she had left something in the oven.",
            "The park was quieter than usual on Tuesday. A few people were walking dogs, and someone had put a small table near the entrance with free books on it. I took a novel and left an old cookbook in its place.",
            "I keep a paper list beside my desk because I forget small tasks when they are only in my phone. Today the list said to buy soap, send the invoice, and call the dentist. I did two of the three.",
            "The meeting started late because the projector would not connect. Once it worked, we went through the budget line by line. There were no major surprises, although we need another conversation about travel costs.",
            "I cooked rice, beans, and the last of the vegetables for lunch. The beans needed more salt than I expected. It was not an exciting meal, but it was warm and filling.",
            "The rain stopped just before we left. The pavement was still wet and the air smelled like leaves. We walked to the shop instead of driving, which took longer but was more pleasant.",
            "I read the instructions twice before assembling the shelf. One of the screws was missing, so I used a spare from the drawer. The shelf leans slightly, but it holds the books."
        ],
    },
    {
        "name": "score separation",
        "criterion": 2,
        "texts": [
            "The weather was cold this morning and I missed the bus. I bought coffee, waited twenty minutes, and arrived at work with wet shoes. Nothing important happened, but I was glad to get home.",
            "The importance of effective communication in the workplace cannot be overstated. Teams that communicate clearly are better positioned to achieve their objectives and avoid costly misunderstandings. There are several strategies organisations can adopt to improve this. First, establishing regular check-ins ensures that information flows consistently between team members. Second, documenting decisions provides a reference point that reduces ambiguity. Finally, encouraging an environment where questions are welcomed helps surface issues early.",
            "A language model can generate polished explanatory prose by selecting probable continuations from a distribution learned over large text collections. The resulting paragraphs often maintain a consistent register, repeat their central framing, and organize each point with explicit transitions. This makes the writing fluent, but fluency alone does not establish authorship.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "The system works well. It handles most cases correctly and provides good results for users.",
            "Right, so. I've been thinking about this since the meeting on Thursday and I still don't have a neat answer, but here's roughly where I've landed. The meeting was useful, though nobody agreed on the next step. I wrote down the bits that seemed important and will ask again tomorrow.",
            "The importance of effective communication in the workplace cannot be overstated. Teams that communicate clearly are better positioned to achieve their objectives and avoid costly misunderstandings. There are several strategies organisations can adopt to improve this. First, establishing regular check-ins ensures that information flows consistently between team members. Second, documenting decisions provides a reference point that reduces ambiguity. Finally, encouraging an environment where questions are welcomed helps surface issues early.",
        ],
    },
    {
        "name": "appeal changes status",
        "criterion": 4,
        "appeals": [
            "The library closes at six, so I returned the books before dinner.",
            "A short note records the decision and gives the team a clear next step.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        if sum(bool(value) for value in (texts, bodies, appeals)) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has multiple input "
                f"collections — pick one"
            )
            continue

        if appeals:
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
