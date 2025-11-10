import unittest

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        vasts = await api.ads.vasts()
        vasts_chain = await api.ads.vasts_chain()

        pprint(object=(
            vasts, 
            vasts_chain
        ))

if __name__ == "__main__":
    unittest.main()