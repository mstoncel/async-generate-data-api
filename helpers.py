from aiohttp import web
from client import Client

async def generate_user(request):
    params = request.rel_url.query
    response = await Client().generate_user(**params)
    return web.json_response(response, status=200, content_type='application/json')