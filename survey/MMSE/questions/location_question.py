from survey.MMSE.questions.question_template import get_question_template


def city_question():
    question = get_question_template()
    question["question id"] = "mmse-location-city"
    question["category"] = "location"
    question["type"] = "city"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def district_question():
    question = get_question_template()
    question["question id"] = "mmse-location-district"
    question["category"] = "location"
    question["type"] = "district"
    question["info"] = "accept district or township"
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 2
    return question
    pass


def road_question():
    question = get_question_template()
    question["question id"] = "mmse-location-road"
    question["category"] = "location"
    question["type"] = "road"
    question["info"] = "accept road or street"
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 2
    return question
    pass
