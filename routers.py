from aiohttp import web
from helpers import generate_user


routes = [
    web.get('/', generate_user),
]

app = web.Application()
app.add_routes(routes)

web.run_app(app)