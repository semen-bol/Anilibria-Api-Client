import unittest

from anilibria_client import AsyncAnilibriaAPI
from anilibria_client.types import SortType, ProductionStatusesType, PublishStatusesType
from anilibria_client.models import Release
from anilibria_client.exceptions import AnilibriaException
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        try:
            """result = await api.anime.catalog_releases_get(
                params=Release(
                    page=1,
                    limit=10,
                    sorting=SortType.RATING_DESC,
                    publish_statuses=[PublishStatusesType.IS_ONGOING],
                    production_statuses=[ProductionStatusesType.IS_IN_PRODUCTION],
                    exclude="poster,description,genres"
                )
            )
            result = await api.anime.catalog_releases_post(
                params=Release(
                    page=1,
                    limit=10,
                    sorting=SortType.RATING_DESC,
                    publish_statuses=[PublishStatusesType.IS_ONGOING],
                    production_statuses=[ProductionStatusesType.IS_IN_PRODUCTION],
                    exclude="poster,description,genres"
                )
            )"""

            age_ratings = await api.anime.catalog_references_age_ratings()
            genres = await api.anime.catalog_references_genres()
            production_statuses = await api.anime.catalog_references_production_statuses()
            publish_statuses = await api.anime.catalog_references_publish_statuses()
            seasons = await api.anime.catalog_references_seasons()
            sorting = await api.anime.catalog_references_sorting()
            types = await api.anime.catalog_references_types()
            years = await api.anime.catalog_references_years()

            result = [age_ratings, genres, production_statuses, publish_statuses, seasons, sorting, types, years]

        except AnilibriaException as e:
            raise e

        pprint(object=(
            result
        ))

if __name__ == "__main__":
    unittest.main()