from flask import Flask, request
import os
from survey import survey_provider


# setup flask
app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))


@app.route("/get_survey", methods=['POST'])
def get_survey():
    # receive json format
    # {"user id":"", "survey type": "mmse", "time": "yyyy/mm/dd"}
    content = request.json
    return survey_provider.generate_survey(content["survey type"], content["user id"])
    pass


@app.route("/commit_survey", methods=['POST'])
def commit_survey():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
