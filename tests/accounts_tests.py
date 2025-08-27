import unittest

from anilibria_client import AsyncAnilibriaAPI
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException
from anilibria_client.types import CollectionType, ContentType, AgeRating
from unittest import IsolatedAsyncioTestCase
from pprint import pprint


class Help:
    async def auth(self, api_without_auth: AsyncAnilibriaAPI):
        try:
            login = str(input("Введите логин: "))
            password = str(input("Введите пароль: "))
            
            res = await api_without_auth.accounts.users_auth_login(login=login, password=password)

            return res.get("token")
        except AnilibriaException as e:
            print(e)
            print("Введены неправильные данные, попробуйте еще раз!")

            await self.auth(api_without_auth=api_without_auth)

class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api_without_auth = AsyncAnilibriaAPI()

        help = Help()
        token = await help.auth(api_without_auth=api_without_auth)

        api_auth = AsyncAnilibriaAPI(authorization=f"Bearer {token}")
        data = await api_auth.accounts.users_me_profile()
        
        age_ratings = await api_auth.accounts.users_me_collections_references_age_ratings()
        genres = await api_auth.accounts.users_me_collections_references_genres()
        types = await api_auth.accounts.users_me_collections_references_types()
        years = await api_auth.accounts.users_me_collections_references_years()
        ids = await api_auth.accounts.users_me_collections_ids()
        releases = await api_auth.accounts.users_me_collections_releases_post(
            type_of_collection=CollectionType.PLANNED, 
            page=1, 
            limit=10, 
            include="id,name.main,genres.name"
        )
        releases_get = await api_auth.accounts.users_me_collections_releases_get(
            type_of_collection=CollectionType.PLANNED,
            page=1,
            limit=10,
            genres="14,29",
            types=[ContentType.MOVIE],
            years="2017",
            search="Мастера Меча Онлайн: Порядковый ранг",
            age_ratings=[AgeRating.R16_PLUS],
            include="id,name.main,genres.name"
        )

        pprint(object=(data, ids))
        

if __name__ == "__main__":
    unittest.main()