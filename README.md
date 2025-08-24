# Anilibria-Api-Client

## Запуск тестов
```bash
py -m tests.название_теста
```

## Тесты
### Пример авторизации (tests/auth_test.py)
```python
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
```
### Пример с использованием двух инициализаций класса и использования execute (tests/execute_tests.py)
```python
import unittest

from anilibria_client import AsyncAnilibriaAPI
from unittest import IsolatedAsyncioTestCase
from pprint import pprint

class TestLikeAJs(IsolatedAsyncioTestCase):
    async def test_methods(self):
        api = AsyncAnilibriaAPI(authorization="Bearer ...")
        anime = await api.execute(endpoint="/anime/releases/random?limit=50&include=id,name.main")
        if len(anime) > 1:
            for rnd in anime:
                pprint(rnd)
        else:
            pprint(anime[0])

class TestAsyncWith(IsolatedAsyncioTestCase):
    async def test_async_with(self):
        async with AsyncAnilibriaAPI(authorization="Bearer ...") as api:
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
```

## Поддержка execute
```python
api = AsyncAnilibriaAPI()
anime = await api.execute(endpoint="/anime/releases/random?limit=50&include=id,name.main")
```

## Ошибки
Для валидации ошибок используйте ```AnilibriaException```, в конкретных случая если вы знаете что делаете можно использовать ```AnilibriaValidationException``` (Ошибка 422)