# Anilibria-Api-Client
## О модуле
### Информация
Anilibria-API-Client - это клиент для работы с API написанный полностью на Python с использованием aiohttp

Позднее будет доступна sync версия, в данный момент ведется разработка async версии и документации когда будет сделана async версия
### Доступные методы
Документация: https://anilibria.top/api/docs/v1#/

Документация модуля: ...

Модуль на PyPI: ...
## Установка
### Терминал
```bash
git clone https://github.com/semen-bol/Anilibria-Api-Client.git
pip install -r requirements.txt
```
### Зависимости
```
aiohttp==3.12.15
pydantic==2.11.7
```
## Использование
### Базовое использование
```python
from anilibria_client import AsyncAnilibriaAPI # Клиент
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Ошибки
from anilibria_client.types import * # Типизация в переменных, * - импорт всего, но рекомендуется импортировать конкретные типы
from anilibria_client.models import * # Модели, в некоторых методах используются модели, * - импорт всего, но рекомендуется импортировать конкретные модели

# Использование
async def main():
    async with AsyncAnilibriaAPI() as api: # Использование через async with
        pass
    api_js_type = AsyncAnilibriaAPI() # Использование Like JS
```
### Структура методов
```
api.{название_подветки}.{полное_название_метода}
```
```python
await api.accounts.users_me_collections_references_age_ratings()
```
Документация: [users_me_collections_references_age_ratings](https://anilibria.top/api/docs/v1#/%D0%90%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D1%8B.%D0%9F%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8.%D0%9C%D0%BE%D0%B5.%D0%9A%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8.%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8/8b157a7586e3c56605e42d0d328ad854)
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
## Issues/Contributing
### Issues
Ознокомившись с форматом Issues во вкладке Issues, идём писать о ошибке которую вы получили
### Contributing
После того как вы форкните репозиторий:

1. Добавьте коммит с изменением в формате всеобщего соглашения о коммитах
2. Откройте пулл реквест и укажите в ревью разработчика
3. Опишите ваши изменения или исправления в проекте

После проверки ваш пулл реквест будет рассмотрен и возможно замёрджен в main ветку