import unittest

from anilibria_api_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        search = await api.app.search_releases(query="Бездомный бог", exclude="poster,age_rating")

        pprint(object=(
            search[0]
        ))

if __name__ == "__main__":
    unittest.main()