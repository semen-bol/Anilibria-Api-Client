import aiohttp
import logging

from .base_api.api_class import AsyncBaseAPI
from typing import Optional, Dict, Any, Optional, Union

from .methods import (
    AccountsMethod,
    AdsMethod,
    AnimeMethod,
    AppMethod,
    MediaMethod,
    TeamsMethod
)

logging.basicConfig(level=logging.ERROR)


class AsyncAnilibriaAPI(AsyncBaseAPI):
    """
    Асинхронный клиент для работы с AnilibriaAPI

    :param base_url: Базовый URL API
    :param authorization: Установить свой токен в формате "Bearer ..."s
    :param proxy: URL прокси-сервера (http://proxy:port или https://proxy:port)
    :param proxy_auth: Аутентификация для прокси (BasicAuth)
    :param proxy_headers: Заголовки для прокси
    """
    def __init__(
            self,
            base_url: str = "https://anilibria.top/api/v1",
            authorization: str = "Bearer",

            proxy: Optional[str] = None,
            proxy_auth: Optional[aiohttp.BasicAuth] = None,
            proxy_headers: Optional[Dict[str, str]] = None,
        ):
        headers = {
            "Content-Type": "application/json",
            "Authorization": authorization
        }

        super().__init__(base_url=base_url, headers=headers, proxy=proxy, proxy_auth=proxy_auth, proxy_headers=proxy_headers)

        self.accounts = AccountsMethod(api=self)
        self.ads = AdsMethod(api=self)
        self.anime = AnimeMethod(api=self)
        self.app = AppMethod(api=self)
        self.media = MediaMethod(api=self)
        self.teams = TeamsMethod(api=self)

    async def execute(
        self,
        endpoint: str,
        method: str = 'GET',
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Создание своего уникального запроса
        
        :param method: Метод используемый для запроса, например GET (обязательно)
        :param endpoint: Конечная точка API (обязательно)
        :param data: Тело запроса
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request(method, endpoint, data=data, json_data=json_data, headers=headers, **kwargs)
    