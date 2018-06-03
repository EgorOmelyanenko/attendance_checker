import json
import requests


def send_request(suffix, data={}):
    return requests.get(
        "http://127.0.0.1:8080/{}".format(suffix),
        data=json.dumps(data),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
            'Content-Encoding': 'utf-8'
        }
    ).json()

print(send_request(
    "lecturer/get_lessons",
    data={"test": "test"})
)
