import unittest
import asyncio

from anilibria_client import AsyncAnilibriaAPI, AnilibriaException
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

        try: 
            data_ = await api_without_auth.accounts.users_me_profile()
        except AnilibriaException:
            data_ = "Ничего нет"

        help = Help()
        token = await help.auth(api_without_auth=api_without_auth)

        api_auth = AsyncAnilibriaAPI(authorization=f"Bearer {token}")
        data = await api_auth.accounts.users_me_profile()

        print("С токеном:")
        print(data)
        
        print("Без токена:")
        print(data_)

if __name__ == "__main__":
    unittest.main()