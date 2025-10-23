import argparse
import asyncio

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.models import Release
from anilibria_api_client.helper import auth #, async_download

async def get_args():
    parser = argparse.ArgumentParser(description="Search anime!")

    parser.add_argument("--name", help="Название аниме", required=True)
    parser.add_argument("--login", help="Логин от аккаунта", required=False)
    parser.add_argument("--password", help="Пароль от аккаунта", required=False)
    parser.add_argument("--limit", help="Лимит выводимых значений, по умолчанию 1")

    return parser.parse_args()

async def get_api_client(login, password):
    if login and password:
        return await auth(AsyncAnilibriaAPI(), login=login, password=password)
    else: return AsyncAnilibriaAPI()

async def main():
    args = await get_args()
    client = await get_api_client(login=args.login, password=args.password)

    data = await client.anime.catalog_releases_get(Release(search=args.name))

    limit = args.limit or 1
    data = data.get("data")[:limit]

    print("Вот что я нашел по запросу {}".format(args.name))
    i = 1

    for item in data:
        detailed = await client.anime.releases_idOrAlias(idOrAlias=item['id'])
        episodes = ""
        i_ = 1
        for episode in detailed.get("episodes"):
            episodes += f"\n{i_}. {episode.get("name") or f"{i_} эпизод"} - {episode.get("hls_1080") or episode.get("hls_720") or episode.get("hls_480")}"
            #await async_download(url=episode.get("hls_1080") or episode.get("hls_720") or episode.get("hls_480"), filename=f"{i_}.mp4")
            i_ += 1
        description = f"""\n{i}. 🌟 {item['name']['main']} ({item['year']}) 🌟

📺 Тип: {item['type']['description']}
🎬 Эпизодов: {item['episodes_total']}
🏷️  Рейтинг: {item['age_rating']['label']}
📅 Сезон: {item['season']['description']} {item['year']}

❤️  В избранном у {item['added_in_users_favorites']} пользователей

Эпизоды: {episodes}"""
        print(description)
        i += 1

    print(f"\nВсего найдено {len(data)} записей")
    return description

if __name__ == "__main__":
    asyncio.run(main())