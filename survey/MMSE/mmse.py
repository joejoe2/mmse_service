from survey.MMSE.questions import time_question, location_question, memory_question, attention_question, language_question, action_question, space_question
import json


def get_questions() -> list:
    questions = []
    # time category
    questions.append(time_question.year_question())
    questions.append(time_question.month_question())
    questions.append(time_question.day_question())
    questions.append(time_question.week_question())
    questions.append(time_question.season_question())
    # location category
    questions.append(location_question.city_question())
    questions.append(location_question.district_question())
    questions.append(location_question.road_question())
    # memory category part 1
    mark = memory_question.mark_question()
    questions.append(mark)
    # attention category
    questions.append(attention_question.sub_seven_question())
    # memory category part 2
    questions.append(memory_question.remind_question(mark["data"]["objects"]))
    # language, space, and action category
    questions.append(language_question.naming_question())
    questions.append(language_question.repeat_question())
    questions.append(action_question.one_action_question())
    questions.append(language_question.make_sentence_question())
    questions.append(space_question.draw_intersections_question())
    questions.append(action_question.three_action_question())
    return questions
    pass


def generate_survey(user_id: str) -> str:
    survey = {
        "user id": user_id,
        "survey type": "mmse",
        "time": "yyyy/mm/dd",
        "questions": get_questions(),
        "total score": 0,
        "full score": 30
    }
    return json.dumps(survey)
    pass
