from survey.MMSE.questions.question_template import get_question_template


def one_action_question():
    question = get_question_template()
    question["question id"] = "mmse-action-one_action"
    question["category"] = "action"
    question["type"] = "one_action"
    question["info"] = "ask user to do one specific action, action type is in data"
    question["data"] = {"type": "shaking device"}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass


def three_action_question():
    question = get_question_template()
    question["question id"] = "mmse-action-three_action"
    question["category"] = "action"
    question["type"] = "three_action"
    question["info"] = "ask user to do three continuous action, action type is in data"
    question["data"] = {"type": "moving a cube to three positions"}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 3
    return question
    pass
