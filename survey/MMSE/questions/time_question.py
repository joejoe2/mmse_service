from survey.MMSE.questions.question_template import get_question_template


def year_question():
    question = get_question_template()
    question["question id"] = "mmse-time-year"
    question["category"] = "time"
    question["type"] = "year"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def month_question():
    question = get_question_template()
    question["question id"] = "mmse-time-month"
    question["category"] = "time"
    question["type"] = "month"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def day_question():
    question = get_question_template()
    question["question id"] = "mmse-time-day"
    question["category"] = "time"
    question["type"] = "day"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def week_question():
    question = get_question_template()
    question["question id"] = "mmse-time-week"
    question["category"] = "time"
    question["type"] = "week"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def season_question():
    question = get_question_template()
    question["question id"] = "mmse-time-season"
    question["category"] = "time"
    question["type"] = "season"
    # question["info"] = ""
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass
