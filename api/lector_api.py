from api.common import get_request, get_response

from classes.lecturer import Lecturer

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
