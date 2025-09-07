import unittest

from anilibria_api_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        all_teams = await api.teams.get(include="title")
        roles = await api.teams.roles(include="title")
        users = await api.teams.users(include="nickname")

        pprint(object=(
            all_teams,
            roles,
            users
        ))

if __name__ == "__main__":
    unittest.main()