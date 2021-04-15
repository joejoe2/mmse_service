from survey.MMSE.questions.question_template import get_question_template
import random


def sub_seven_question():
    question = get_question_template()
    question["question id"] = "mmse-attention-sub_seven"
    question["category"] = "attention"
    question["type"] = "sub_seven"
    question["info"] = "use start number to ask user, startNum-subNum=ans1, ans1-subNum=ans2, ... until get ans5. the " \
                       "ans1-5 will depend on startNum and subNum"
    question["data"] = {"startNum": random_start_number(), "subNum": random_sub_number()}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 5
    return question
    pass


def random_start_number():
    return random.choice(range(100, 150))
    pass


def random_sub_number():
    return random.choice(range(3, 8))
    pass
