import unittest

from anilibria_api_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        prom = await api.media.promotions(include="id")
        vid = await api.media.videos(include="id")

        pprint(object=(
            prom,
            vid
        ))

if __name__ == "__main__":
    unittest.main()