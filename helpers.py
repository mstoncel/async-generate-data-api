from aiohttp import web
from client import Client
from adapter import Adapter

async def generate_user(request):
    params = request.rel_url.query
    response = await Adapter().generate_user(params=params)
    return web.json_response(
                    response, status=200, 
                    content_type='application/json')