import unittest

from anilibria_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        search = await api.app.search_releases(query="Клинок рассекающий демонов: Беско")
        status = await api.app.status()

        pprint(object=(
            search[0].get("name").get("main"), 
            status.get("is_alive")
        ))

if __name__ == "__main__":
    unittest.main()