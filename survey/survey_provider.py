import survey.MMSE.mmse


def generate_survey(survey_type: str, user_id: str) -> str:
    if survey_type == "mmse":
        return survey.MMSE.mmse.generate_survey(user_id)
    pass
