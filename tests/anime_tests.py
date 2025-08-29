import unittest

from anilibria_client import AsyncAnilibriaAPI
from anilibria_client.types import SortType, ProductionStatusesType, PublishStatusesType
from anilibria_client.models import Release
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

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
        result = await api.anime.catalog_releases_post(
            params=Release(
                page=1,
                limit=10,
                sorting=SortType.RATING_DESC,
                publish_statuses=[PublishStatusesType.IS_ONGOING],
                production_statuses=[ProductionStatusesType.IS_IN_PRODUCTION],
                exclude="poster,description,genres"
            )
        )

        pprint(object=(
            result
        ))

if __name__ == "__main__":
    unittest.main()