from survey.MMSE.questions.question_template import get_question_template
import random


def mark_question():
    question = get_question_template()
    question["question id"] = "mmse-memory-mark"
    question["category"] = "memory"
    question["type"] = "mark"
    question["info"] = "show user there are three random objects and let him repeat(the objects will be used in later " \
                       "question) "
    question["data"] = {"objects": random_three_objects()}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 3
    return question
    pass


def remind_question(mark_objects):
    question = get_question_template()
    question["question id"] = "mmse-memory-remind"
    question["category"] = "memory"
    question["type"] = "remind"
    question["info"] = "ask user to remind the three objects in previous mark question"
    question["data"] = {"objects": mark_objects}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 3
    return question
    pass


def random_three_objects():
    obj1 = random.choice(["櫻花", "鼻子", "眼睛"])
    obj2 = random.choice(["火車", "汽車", "船"])
    obj3 = random.choice(["貓", "太陽", "星星"])
    return [obj1, obj2, obj3]
    pass
