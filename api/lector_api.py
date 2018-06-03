from api.common import get_request, get_response
from server import server_settings

from classes.lecturer import Lecturer
from qr.qr import generate_qr as gen_qr

LECTORS = []

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

    return get_response(
        data={
            "image": "{}:{}/static/{}/img.jpg".format(
                server_settings["host"],
                server_settings["port"],
                req_data["id"]
            )}
        )
