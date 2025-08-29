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