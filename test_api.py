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

## залогинить препода, вернет токен, на вход логин и пас который есть в БД, 
## смотри database/database.py в комментах
# id_ = send_request(
#     "lector/auth",
#     data={
#         "username": "romanov",
#         "password": "12345678"
#     })

# взять список студентов на текущей лекции.
result = send_request(
    "lector/get__list",
    data={
        "id": 91
    })

print(result)

# залогинить студента, вернет токен, на вход логин и пас с nstu.ru
# token = send_request(
#     "student/auth",
#     data={
#         "username": "avgustan.2016@stud.nstu.ru",
#         "password": "0123456789a!"
#     })

# # инфа про студента, на вход - токен
# result = send_request(
#     "student/students__info",
#     data={
#         "token": token["data"]
#     })

# print(result)

# отправить qr код студентом
# result = send_request(
#     "student/send_qr",
#     data={
#         "token": token["data"],
#         "string": "SolusRex"
#     })

# print(result)


# # взять текущую пару, принимает токен и дату, если нужно ее подменить
# result = send_request(
#     "student/current__pair",
#     data={
#         "token": token["data"],
#         "date": "2018-05-29 11:59:35"
#     })
# print(result)



## генерирует qr-код, на вход id препода и строку, которую шифруем, на выходе url
## 127.0.0.1:8080/static/91/img.jpg по нему забираем картинку.
## если нужно в папке static всякую дичь можешь хранить статическую
# send_request(
#     "lector/generate__qr",
#     data={
#         "id": "91",
#         "string": "123"
#     })
