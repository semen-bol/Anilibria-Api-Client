# Anilibria-Api-Client
## О модуле
### Доступные методы
Документация: https://anilibria.top/api/docs/v1#/

Методы:
```
GET
POST
DELETE
```

Из них сейчас доступны (позднее будет перенесено в Wiki):
```python
await api.accounts.otp_accept()
await api.accounts.otp_get()
await api.accounts.users_auth_login()
await api.accounts.users_auth_logout()
await api.accounts.users_auth_password_forget()
await api.accounts.users_auth_password_reset()
await api.accounts.users_auth_social_authenticate()
await api.accounts.users_auth_social_login()
await api.accounts.users_me_collections_references_age_ratings()
await api.accounts.users_me_collections_references_genres()
await api.accounts.users_me_collections_references_types()
await api.accounts.users_me_collections_references_years()
await api.accounts.users_me_collections_ids()
await api.accounts.users_me_collections_releases_get()
await api.accounts.users_me_collections_releases_post()
```
## Установка
### Терминал
```bash
git clone repo
```
```bash
pip install -r requirements.txt
```
### Зависимости
```
aiohttp==3.12.15
```
### Код
```python
from anilibria_client import AsyncAnilibriaAPI # Клиент
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Ошибкит
from anilibria_client.types import CollectionType, ContentType, AgeRating # Типизация в переменных

# Использование
async def main():
    async with AsyncAnilibriaAPI() as api:
        pass
    api_js_type = AsyncAnilibriaAPI()
```

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
```
### Пример использования Accounts (tests/accounts_tests.py)
```python
import unittest

from anilibria_client import AsyncAnilibriaAPI, AnilibriaException
from anilibria_client.types import *
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

        pprint(object=(data, age_ratings, genres, types, years, releases, releases_get))
        

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