from aiohttp.web import Response

import json


async def get_request(request):
    return await request.json()

def get_response(data={}, error_flag=False):
    return Response(
        body = json.dumps({
            "data": data,
            "error_flag": error_flag
        })
    )
