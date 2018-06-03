from api.common import get_request, get_response
from nstu_api.NSTUTRPOAPI.NSTUAPI import NSTUAPI, OperationResult

STATE = {}

async def auth(request):
    req_data = await get_request(request)

    result = NSTUAPI().auth_user(
        req_data["username"],
        req_data["password"]
    )

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

