import logging

from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_request import Request
from aiohttp import web

from hack.config import INDEX_PATH

log = logging.getLogger(__name__)


async def get_root(request: Request) -> FileResponse:  # noqa
    return FileResponse(INDEX_PATH)


async def get_template(request: Request) -> FileResponse:
    return FileResponse(INDEX_PATH)


async def health_check(request: Request) -> web.Response:
    return web.json_response({'status': 'ok'}, status=200)
