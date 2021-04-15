import requests
import json

res = requests.post('http://localhost:8080/get_survey', json={"user id": "test", "survey type": "mmse", "time": "yyyy/mm/dd"})
if res.ok:
    print(res.text)
    survey=json.loads(res.text)
    questions=survey["questions"]
    score=0
    for q in questions:
        print(q)
        score+=q["full score"]
    print(30==score)
