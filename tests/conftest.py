import pytest
import typing as t

from hack.app import make_app


@pytest.fixture
async def app_server(aiohttp_server: t.Any) -> t.Any:
    app = await make_app()
    return await aiohttp_server(app)


@pytest.fixture
async def client(aiohttp_client: t.Any, app_server: t.Any) -> t.Any:
    client = await aiohttp_client(app_server)
    return client
