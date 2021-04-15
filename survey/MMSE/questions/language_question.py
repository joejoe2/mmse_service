from survey.MMSE.questions.question_template import get_question_template
import random


def naming_question():
    question = get_question_template()
    question["question id"] = "mmse-language-naming"
    question["category"] = "language"
    question["type"] = "naming"
    question["info"] = "show two objects picture and ask for their name"
    question["data"] = {"objects": random_naming_objects()}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 2
    return question
    pass


def random_naming_objects():
    obj1 = random.choice(["貓", "太陽", "蘋果"])
    obj2 = random.choice(["鼻子", "眼睛", "香蕉"])
    return [obj1, obj2]
    pass


def repeat_question():
    question = get_question_template()
    question["question id"] = "mmse-language-repeat"
    question["category"] = "language"
    question["type"] = "repeat"
    question["info"] = "make a sentence and ask user to repeat it"
    question["data"] = {"sentence": random_sentence()}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def random_sentence():
    sentences = ["天生我才必有用", "舉頭三尺有神明"]
    return random.choice(sentences)
    pass


def make_sentence_question():
    question = get_question_template()
    question["question id"] = "mmse-language-make_sentence"
    question["category"] = "language"
    question["type"] = "make_sentence"
    question["info"] = "ask user to make a sentence, options are in data"
    question["data"] = {"sentence": get_filling_sentence_blocks()}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def get_filling_sentence_blocks():
    s = random.choice(["我", "你", "他"])
    t = random.choice(["今天", "昨天", "剛剛"])
    v = random.choice(["買了", "吃了", "煮了"])
    n = random.choice(["一條魚", "一隻雞腿", "一盤水果"])
    return [s, t, v, n]
    pass
