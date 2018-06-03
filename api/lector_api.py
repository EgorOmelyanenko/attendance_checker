from api.common import get_request, get_response
from server import server_settings

from classes.lecturer import Lecturer
from qr.qr import generate_qr as gen_qr
from database.database import Postgres

LECTORS = []
QR = ["SolusRex"]

async def auth(request):
    req_data = await get_request(request)

    lector = Lecturer(name=req_data["username"])
    LECTORS.append(lector)
    return get_response(
        data={
            "id": lector.authorize(req_data["password"])
            }
        )

async def generate_qr(request):
    req_data = await get_request(request)
    gen_qr(req_data["id"], req_data["string"])
    global QR
    QR.append(req_data["string"])

    return get_response(
        data={
            "image": "{}:{}/static/{}/img.jpg".format(
                server_settings["host"],
                server_settings["port"],
                req_data["id"]
            )}
        )

async def get_students_list(request):
    result = {}
    students = Postgres.select(table="pairs", where=("pair_id='{}'".format(1)))
    for student in students:
        group_id = Postgres.select(table="group_students", where="student_id='{}'".format(student["student_id"]))[0]["group_id"]
        result.update(
            {
                "student": Postgres.select(table="student", where="student_id='{}'".format(student["student_id"]))[0]["student_info"],
                "group": Postgres.select(table="groups", where="group_id='{}'".format(group_id))[0]["group_info"]
            }
        )

    print(result)
    return get_response(
        data=result
        )
