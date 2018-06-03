from api.common import get_request, get_response
from nstu_api.NSTUTRPOAPI.NSTUAPI import NSTUAPI, OperationResult



async def auth(request):
    req_data = await get_request(request)

    result = NSTUAPI().auth_user(
        req_data["username"],
        req_data["password"]
    )

    return _response(result, True)

async def get_info(request):
    req_data = await get_request(request)

    result = NSTUAPI().get_student_info(
        req_data["token"],
    )

    return _response(result, True)

# private

def _response(result, response_data_flag=False):
    error_flag = False if result[0] == OperationResult.SUCCESSFUL else True
    data = result[1] if response_data_flag else {}

    return get_response(data=data, error_flag=error_flag)
