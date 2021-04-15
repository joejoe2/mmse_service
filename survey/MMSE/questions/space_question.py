from survey.MMSE.questions.question_template import get_question_template


def draw_intersections_question():
    question = get_question_template()
    question["question id"] = "mmse-space-draw_intersections"
    question["category"] = "space"
    question["type"] = "draw_intersections"
    question["info"] = "ask user to draw two pentagons intersecting quadratically"
    # question["data"] = {}
    # question["user answer"] = {}
    # question["user score"] = 0
    question["full score"] = 1
    return question
    pass
