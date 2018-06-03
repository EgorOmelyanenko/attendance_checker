import json

from aiohttp.web import Response

from nstu_api.NSTUTRPOAPI.NSTUAPI import OperationResult


async def get_request(request):
    return await request.json()

def get_response(result={}, data={}, response_data_flag=False):
    error_flag = False

    if result:
        if result[0] != OperationResult.SUCCESSFUL:
            error_flag = True
    
        if response_data_flag:
            data = result[1]

    return _response(data=data, error_flag=error_flag)

def _response(data={}, error_flag=False):
    return Response(
        body = json.dumps({
            "data": data,
            "error_flag": error_flag
        })
    )
