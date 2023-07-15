
from sawal import Questions


prompts = [
    "What color are the apple?\n(a) Red\n(b) Purple \n(c) Orange\n\n",
    "What color are the bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are the strawberries?\n(a) Yellow\n(b) Red\n(c) Blues\n\n"
]

questions = [
    Questions(prompts[0], "a"),
    Questions(prompts[1], "c"),
    Questions(prompts[2], "b"),
]


def test_run(questions):
    score = 0
    for question in questions:
        answer = input(question.quest)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


test_run(questions)
