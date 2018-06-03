from api.common import get_request, get_response
from classes.lecturer import Lecturer


async def get_lessons(request):
    req_data = await get_request(request)
    return get_response(data={"foo": "pass"})
