# Anilibria-Api-Client

[![pypi](https://img.shields.io/badge/anilibria_api_client_on_PyPi-blue)]()
![version](https://img.shields.io/badge/Version-0.1.1-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![python](https://img.shields.io/badge/Python-3.13%2B-blue)

> [!CAUTION]  
> **It is not an official wrapper.** [Official AniLibria's Swagger](https://anilibria.top/api/docs/v1)

Anilibria-API-Client - this a async client to work with Anilibria API, use a aiohttp. Full writed at python

U can download anime too fast!

## Installing
Tested at python 3.13
### pip
```bash
$ pip install anilibria-api-client
```
## Usage
```python
from anilibria_client import AsyncAnilibriaAPI # Client
from anilibria_client.exceptions import AnilibriaException, AnilibriaValidationException # Errors
from anilibria_client.types import * # Types for some methods
from anilibria_client.models import * # Models for some methods
from anilibria_client.helper import * # Download anime, save torrents files and more

async def main():
    async with AsyncAnilibriaAPI() as api: # async with
        await api.teams.users(include="nickname")

    api = AsyncAnilibriaAPI() # like js support
    await api.teams.users(include="nickname")
```

## Documentation 📃
Docs..
## Issues/Contributing
### Issues
Report for any issues [here](https://github.com/semen-bol/Anilibria-Api-Client/issues)
### Contributing
We allow contributing! Read the [CODE_OF_CONDUCT.md](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/CODE_OF_CONDUCT.md)

## License 📄
Anilibria-Api-Client is [MIT](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/LICENSE) licenced.