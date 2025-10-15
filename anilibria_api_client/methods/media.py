from ._libria import BaseMethod
from typing import Optional


class MediaMethod(BaseMethod):
    async def promotions(
            self,
            include: Optional[str] = None,
            exclude: Optional[str] = None
    ):
        """
        Возвращает список промо-материалов или рекламные кампании в случайном порядке

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }
        
        return await self._api.get("/media/promotions", params=params)
    
    async def videos(
            self,
            limit: Optional[int] = None,
            include: Optional[str] = None,
            exclude: Optional[str] = None
    ):
        """
        Возвращает список последних видео-роликов

        :param limit: Лимит возвращаемых полей
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "limit": limit,
            "include": include,
            "exclude": exclude
        }
        
        return await self._api.get("/media/videos", params=params)