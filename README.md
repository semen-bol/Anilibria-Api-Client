# Anilibria-Api-Client
## О модуле
### Информация
Anilibria-API-Client - это клиент для работы с API написанный полностью на Python с использованием aiohttp

Позднее будет доступна sync версия, в данный момент ведется разработка async версии и документации когда будет сделана async версия
### Доступные методы
Документация: https://anilibria.top/api/docs/v1#/

Документация модуля: ...
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
### Базовое использование
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