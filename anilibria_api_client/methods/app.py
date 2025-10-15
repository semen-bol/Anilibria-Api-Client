from ._libria import BaseMethod
from typing import Optional


class AppMethod(BaseMethod):
    async def search_releases(
            self,
            query: str,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает данные по релизам, которые удовлетворяют поисковому запросу

        :param query: Обязательный параметр. Строка поиска
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "query": query,
            "include": include,
            "exclude": exclude
        }

        return await self._api.get("/app/search/releases", params=params)
    
    async def status(
            self
    ):
        """
        Возвращает информацию о статусе API
        """
        return await self._api.get("/app/status")