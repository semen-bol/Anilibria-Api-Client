from ._libria import BaseMethod
from ._helper import validate_filters, create_filters_from_release
from ..models import Release
from typing import Optional


class AnimeMethod(BaseMethod):
    async def catalog_releases_get(
            self,
            params: Release
    ):
        """
        Возвращает список релизов по заданными параметрам (GET запрос)

        :param params: Тело Release
        """
        body = {
            "page": params.page,
            "limit":params.limit,
            "include": params.include,
            "exclude": params.exclude,
        }
        validated_f_args = await validate_filters(params=params)
        final_body = {**body, **validated_f_args}

        return await self._api.get("/anime/catalog/releases", params=final_body)
    
    async def catalog_releases_post(
            self,
            params: Release
    ):
        """
        Возвращает список релизов по заданными параметрам (POST запрос)

        :param params: Тело Release
        """
        body = {
            "page": params.page,
            "limit":params.limit,
            "include": params.include,
            "exclude": params.exclude,
        }
        filters = await create_filters_from_release(params)
        final_body = {**body, **filters}

        return await self._api.post("/anime/catalog/releases", json_data=final_body)
    
    async def catalog_references_age_ratings(
            self
    ):
        """
        Возвращает список возможных возрастных рейтингов в каталоге
        """
        return await self._api.get("/anime/catalog/references/age-ratings")
    
    async def catalog_references_genres(
            self
    ):
        """
        Возвращает список всех жанров в каталоге
        """
        return await self._api.get("/anime/catalog/references/genres")
    
    async def catalog_references_production_statuses(
            self
    ):
        """
        Возвращает список возможных статусов озвучки релиза в каталоге
        """
        return await self._api.get("/anime/catalog/references/production-statuses")
    
    async def catalog_references_publish_statuses(
            self
    ):
        """
        Возвращает список возможных статусов выхода релиза в каталоге
        """
        return await self._api.get("/anime/catalog/references/publish-statuses")
    
    async def catalog_references_seasons(
            self
    ):
        """
        Возвращает список возможных сезонов релизов в каталоге
        """
        return await self._api.get("/anime/catalog/references/seasons")
    
    async def catalog_references_sorting(
            self
    ):
        """
        Возвращает список возможных типов сортировок в каталоге
        """
        return await self._api.get("/anime/catalog/references/sorting")
    
    async def catalog_references_types(
            self
    ):
        """
        Возвращает список возможных типов релизов в каталоге
        """
        return await self._api.get("/anime/catalog/references/types")
    
    async def catalog_references_years(
            self
    ):
        """
        Возвращает список годов в каталоге
        """
        return await self._api.get("/anime/catalog/references/years")
    
    async def franchises(
            self,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список франшиз

        Args:
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }
        return await self._api.get("/anime/franchises", params=params)
    
    async def franchises_franchiseId(
            self,
            franchiseId: str,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает данные франшизы по Id

        Args:
            franchiseId: Обязательно. Id франшизы
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }

        endpoint = self._api.build_endpoint_with_params("/anime/franchises/{franchiseId}", franchiseId=franchiseId)
        return await self._api.get(endpoint=endpoint, params=params)
    
    async def franchises_random(
            self,
            limit: Optional[int] = None,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список случайных франшиз.

        Args:
            limit: Лимит случайных франшиз
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "limit": limit,
            "include": include,
            "exclude": exclude
        }
        
        return await self._api.get("/anime/franchises/random", params=params)
    
    async def franchises_release_releaseId(
            self,
            releaseId: str,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список франшиз, в которых участвует релиз

        Args:
            releaseId: Обязательно. Id франшизы
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }

        endpoint = self._api.build_endpoint_with_params("/anime/franchises/release/{releaseId}", releaseId=releaseId)
        return await self._api.get(endpoint=endpoint, params=params)
    
    async def genres(
            self,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список всех жанров

        Args:
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }
        
        return await self._api.get("/anime/genres", params=params)
    
    async def genres_genreId(
            self,
            genreId: int,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список всех жанров

        Args:
            genreId: ID жанра, обязательно
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "include": include,
            "exclude": exclude
        }
        
        endpoint = self._api.build_endpoint_with_params("/anime/genres/{genreId}", genreId=genreId)
        return await self._api.get(endpoint, params=params)
    
    async def genres_random(
            self,
            limit: Optional[int] = None,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список случайных жанров

        Args:
            limit: Лимит случайных жанров
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "limit": limit,
            "include": include,
            "exclude": exclude
        }

        return await self._api.get("/anime/genres/random", params=params)
    
    async def genres_genreId_releases(
            self,
            genreId: int,
            page: Optional[int] = None,
            limit: Optional[int] = None,
            include: Optional[str] = None,
            exclude: Optional[str]  = None
    ):
        """
        Возвращает список всех релизов жанра

        Args:
            genreId: Обязательно. ID жанра
            page: Номер страницы
            limit: Лимит на страницу
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude
        }

        endpoint = self._api.build_endpoint_with_params("/anime/genres/{genreId}/releases", genreId=genreId)
        return await self._api.get(endpoint, params=params)