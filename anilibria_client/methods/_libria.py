from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ..api_client import AsyncAnilibriaAPI

class BaseMethod:
    def __init__(self, api: 'AsyncAnilibriaAPI'):
        self._api = api
    