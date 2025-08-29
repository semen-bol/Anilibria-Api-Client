import unittest

from anilibria_client import AsyncAnilibriaAPI
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException
from anilibria_client.types import *
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