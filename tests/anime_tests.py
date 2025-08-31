import unittest

from anilibria_client import AsyncAnilibriaAPI
from anilibria_client.types import SortType, ProductionStatusesType, PublishStatusesType, ContentType
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
            )"""
            """release = await api.anime.catalog_releases_post(
                params=Release(
                    page=1,
                    limit=1,
                    search="Бездомный бог",
                    types=[ContentType.TV],
                    exclude="poster,description,genres"
                )
            )"""

            """age_ratings = await api.anime.catalog_references_age_ratings()
            genres = await api.anime.catalog_references_genres()
            production_statuses = await api.anime.catalog_references_production_statuses()
            publish_statuses = await api.anime.catalog_references_publish_statuses()
            seasons = await api.anime.catalog_references_seasons()
            sorting = await api.anime.catalog_references_sorting()
            types = await api.anime.catalog_references_types()
            years = await api.anime.catalog_references_years()

            result = [age_ratings, genres, production_statuses, publish_statuses, seasons, sorting, types, years]"""

            """fr = await api.anime.franchises(include="id")
            random = await api.anime.franchises_random(limit=1, include="id")

            find = await api.anime.franchises_franchiseId(random[0].get("id"), include="franchise_releases")
            find_release = await api.anime.franchises_release_releaseId(find.get("franchise_releases")[0].get("release_id"))"""

            """result = await api.anime.genres()
            sr = await api.anime.genres_genreId(result[5].get("id"))"""

            """sr = await api.anime.genres_random(limit=1)
            sr2 = await api.anime.genres_genreId_releases(sr[0].get("id"))"""

        except AnilibriaException as e:
            raise e

        pprint(object=(
            "here your test"
        ))

if __name__ == "__main__":
    unittest.main()