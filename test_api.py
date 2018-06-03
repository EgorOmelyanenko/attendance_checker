import json
import requests


def send_request(suffix, data={}):
    return requests.post(
        "http://127.0.0.1:8080/{}".format(suffix),
        data=json.dumps(data),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
            'Content-Encoding': 'utf-8'
        }
    ).json()

r = send_request(
    "student/auth",
    data={
        "username": "d.bogomolov@corp.nstu.ru",
        "password": "jmXQF97J"
    })["data"] ## get token


print(send_request(
    "student/students__info",
    data={
        "token": r
    })
)
