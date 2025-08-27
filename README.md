# Anilibria-Api-Client
## О модуле
### Доступные методы
Документация: https://anilibria.top/api/docs/v1#/

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
## Использование
### Базовое использование (два примера)
```python
from anilibria_client import AsyncAnilibriaAPI # Клиент
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Ошибкит
from anilibria_client.types import CollectionType, ContentType, AgeRating # Типизация в переменных

# Использование
async def main():
    async with AsyncAnilibriaAPI() as api: # Использование через async with
        pass
    api_js_type = AsyncAnilibriaAPI() # Использование Like JS
```

## Поддержка execute
```python
api = AsyncAnilibriaAPI()
anime = await api.execute(endpoint="/anime/releases/random?limit=50&include=id,name.main")
```

## Ошибки
### Базовая валидация ошибок
```python
from anilibria_client.exceptions import AnilibriaException

try: 
    data = await api.accounts.users_me_profile()
except AnilibriaException:
    data = "Ничего нет"

```