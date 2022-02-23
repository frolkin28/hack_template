from aiohttp import web

from hack.handlers import (
    health_check,
    get_root,
    get_template,
)


def setup_routes(app: web.Application) -> None:

    # health check
    app.router.add_get('/health', health_check)

    # views
    app.router.add_get('/', get_root)
    app.router.add_get('/{tail:(?!api/)(.+)}/', get_template)
