from aiohttp import web
from .route import routes

async def web_server():
    app = web.Application(client_max_size=30000000)
    app.add_routes(routes)
    return app
