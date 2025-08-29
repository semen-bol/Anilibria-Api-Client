# Anilibria-Api-Client

[![pypi](https://img.shields.io/badge/anilibria_api_client_on_PyPi-blue)]()
![version](https://img.shields.io/badge/Version-0.1.0-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![python](https://img.shields.io/badge/Python-3.13%2B-blue)

> [!CAUTION]  
> **It is not an official wrapper.** [Official AniLibria's Swagger](https://anilibria.top/api/docs/v1)

Anilibria-API-Client - это клиент для работы с API написанный полностью на Python с использованием aiohttp

## Установка
### pip
```bash
$ pip install anilibria-api-client
```
## Использование
```python
from anilibria_client import AsyncAnilibriaAPI # Клиент
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Ошибки
from anilibria_client.types import * # Типизация в переменных, * - импорт всего, но рекомендуется импортировать конкретные типы
from anilibria_client.models import * # Модели, в некоторых методах используются модели, * - импорт всего, но рекомендуется импортировать конкретные модели

# Использование
async def main():
    async with AsyncAnilibriaAPI() as api: # Использование через async with
        await api.teams.users(include="nickname")
        
    api_js_type = AsyncAnilibriaAPI() # Использование Like JS
    await api_js_type.teams.users(include="nickname")
```

## Documentation 📃
Docs..

## Issues/Contributing
### Issues
[Issues](https://github.com/semen-bol/Anilibria-Api-Client/issues)
### Contributing
We allow contributing! Read the [CODE_OF_CONDUCT.md](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/CODE_OF_CONDUCT.md)

## License 📄
Anilibria-Api-Client is [MIT](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/LICENSE) licenced.