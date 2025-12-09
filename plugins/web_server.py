from aiohttp import web
from .route import routes

async def start_web_server():
    app = web.Application()
    app.add_routes(routes)
    return app
