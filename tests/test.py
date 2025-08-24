import unittest

from anilibria_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase

class TestMethod(IsolatedAsyncioTestCase):
    async def test_methods(self):
        async with AsyncAnilibriaAPI(authorization="Bearer eyJpdiI6IlRvejBxYjV1QzZLZWZoK0RoRVRkc3c9PSIsInZhbHVlIjoidU5VQlJiSW56SENHUHJTM0Z4dHdFZHFuc0dCbmhYOWk4akVDMnovMENBRUc5Y1RtUTh0UzdoN3AwR0F6Ync4ZyIsIm1hYyI6Ijk2YmY4ZmJhOTM3ZDllOWYyNzgzMGQ4OTAzYjk4MjJjNWVhNjA1YjIxZTBhYmVkZWFhMDExZGMxMTI0MjQzYjgiLCJ0YWciOiIifQ==") as api:
            res = await api.accounts.users_me_profile()
            print(res)

if __name__ == "__main__":
    unittest.main()