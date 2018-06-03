from aiohttp.web import Response

import json


async def get_request(request):
    return await request.json()

def get_response(data={}):
    return Response(
        body=json.dumps(data)
    )
