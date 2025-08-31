from ._libria import BaseMethod
from ._helper import validate_filters, create_filters_from_release
from ..models import Release


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