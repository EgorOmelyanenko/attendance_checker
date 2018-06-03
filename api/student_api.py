from api.common import get_request, get_response
from nstu_api.NSTUTRPOAPI.NSTUAPI import NSTUAPI, OperationResult
from classes.student import Student
from api.lector_api import QR, LECTORS
from database.database import Postgres

STUDENTS=[]

async def auth(request):
    req_data = await get_request(request)

    global STUDENTS

    result = NSTUAPI().auth_user(
        req_data["username"],
        req_data["password"]
    )
    if len(result) > 1:
        STUDENTS.append(Student(req_data["username"], result[1]))

    return get_response(result, True)

async def get_info(request):
    req_data = await get_request(request)

    result = NSTUAPI().get_student_info(
        req_data["token"],
    )

    return get_response(result, True)

async def get_current_pair(request):
    req_data = await get_request(request)

    result = NSTUAPI().get_current_pair(
        req_data["token"],
        date=req_data["date"] if "date" in req_data else None
    )

    return get_response(result, True)

async def send_qr(request):
    req_data = await get_request(request)
    if req_data["string"] in QR:
        lector_id = LECTORS[0].get_id()
        pair_id = LECTORS[0].get_current_pair()
        student_ = NSTUAPI().get_student_info(
            req_data["token"],
        )[1]
        student = Postgres.select(table="student", where="student_info='{}'".format(student_['FIO']))[0]
        # group_ = Postgres.select(
        #     table="group_students",
        #     where="student_id='{}'".format(student['student_id']))[0]
        
        # group = Postgres.select(table="groups", where="group_id='{}'".format(group_["group_id"]))[0]
        # Postgres.insert(table="current_pars", [lector_id, pair_id, student["student_info"]])
        print(lector_id, pair_id, student["student_info"], student['student_id'])
        Postgres.insert(table="pairs", values=[lector_id, pair_id, student['student_id']])

        return get_response()
