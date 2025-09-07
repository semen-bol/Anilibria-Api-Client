import unittest

from anilibria_api_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint

class TestLikeAJs(IsolatedAsyncioTestCase):
    async def test_methods(self):
        api = AsyncAnilibriaAPI()
        anime = await api.execute(endpoint="/anime/releases/random?limit=50&include=id,name.main")
        if len(anime) > 1:
            for rnd in anime:
                pprint(rnd)
        else:
            pprint(anime[0])

class TestAsyncWith(IsolatedAsyncioTestCase):
    async def test_async_with(self):
        async with AsyncAnilibriaAPI() as api:
            list = ""
            anime = await api.execute(endpoint="/anime/releases/random?limit=50&include=id,name.main")
            if len(anime) > 1:
                for rnd in anime:
                    list += f"{str(rnd.get("name").get("main"))}, "
            else:
                list += str(anime.get("name").get("main"))

            print(list)


if __name__ == "__main__":
    unittest.main()