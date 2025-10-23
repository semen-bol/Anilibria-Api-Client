import unittest

from anilibria_api_client import AsyncAnilibriaAPI
from anilibria_api_client.types import SortType, ProductionStatusesType, PublishStatusesType, ContentType
from anilibria_api_client.models import Release
from anilibria_api_client.exceptions import AnilibriaException
from anilibria_api_client.helper import auto_paginate, async_download, auth, download_torrent_file
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
            print("Введены неправильные данные, попробуйте еще раз!")

            return await self.auth(api_without_auth=api_without_auth)

class Test(IsolatedAsyncioTestCase):
    async def test(self):
        api = AsyncAnilibriaAPI()

        """help = Help()
        token = await help.auth(api_without_auth=api)

        api_auth = AsyncAnilibriaAPI(authorization=f"Bearer {token}")"""

        try:
            result = await api.anime.catalog_releases_get(
                params=Release(
                    page=1,
                    limit=10,
                    sorting=SortType.RATING_DESC,
                    publish_statuses=[PublishStatusesType.IS_ONGOING],
                    production_statuses=[ProductionStatusesType.IS_IN_PRODUCTION],
                    exclude="poster,description,genres"
                )
            )
            """release = await api.anime.catalog_releases_post(
                params=Release(
                    page=1,
                    limit=1,
                    search="Бездомный бог",
                    types=[ContentType.TV],
                    exclude="poster,description,genres"
                )
            )"""

            """age_ratings = await api.anime.catalog_references_age_ratings()
            genres = await api.anime.catalog_references_genres()
            production_statuses = await api.anime.catalog_references_production_statuses()
            publish_statuses = await api.anime.catalog_references_publish_statuses()
            seasons = await api.anime.catalog_references_seasons()
            sorting = await api.anime.catalog_references_sorting()
            types = await api.anime.catalog_references_types()
            years = await api.anime.catalog_references_years()

            result = [age_ratings, genres, production_statuses, publish_statuses, seasons, sorting, types, years]"""

            """fr = await api.anime.franchises(include="id")
            random = await api.anime.franchises_random(limit=1, include="id")

            find = await api.anime.franchises_franchiseId(random[0].get("id"), include="franchise_releases")
            find_release = await api.anime.franchises_release_releaseId(find.get("franchise_releases")[0].get("release_id"))"""

            """result = await api.anime.genres()
            sr = await api.anime.genres_genreId(result[5].get("id"))"""

            """sr = await api.anime.genres_random(limit=1)
            sr2 = await api.anime.genres_genreId_releases(sr[0].get("id"))"""

            """alls = await api.anime.releases_latest(1)
            rnd = await api.anime.releases_random(1)
            recm = await api.anime.releases_recommended(1)
            list = await api.anime.releases_list(ids=[9951, 9433, 5692], aliases=["darling-in-the-franxx"])"""
            #srh = await api.anime.releases_idOrAlias(idOrAlias="darling-in-the-franxx")
            """r = await api.anime.releases_idOrAlias_members(idOrAlias="darling-in-the-franxx")
            fr = await api_auth.anime.releases_idOrAlias_episodes_timecodes(idOrAlias="darling-in-the-franxx")"""

            """fr = await api.anime.releases_episodes_releaseEpisodeId(releaseEpisodeId="9f557020-0a14-4d0f-ab33-5a5e3a2e6c79", include="release.episodes.hls_720,release.episodes.hls_420,release.episodes.hls_1080")
            i = 1

            for a in fr.get("release").get("episodes"):
                await async_download(url=a.get("hls_1080"), filename=f"{i}.mp4")
                i += 1"""
            
            """torrents = await api.anime.torrents()
            torrent = await api.anime.torrents_hashOrId(torrents.get("data")[0].get("hash")) # Первый торрент, далее работает по нему

            torrent_hash = await api.anime.torrents_hashOrId_file(torrent.get("hash"))
            download_status = await download_torrent_file(torrent_hash, torrent.get("label"))"""

            """res2 = await api.anime.schedule_week(include="release.id")"""
            """res = await api.anime.torrents_rss_release_releaseId(9995)"""

        except AnilibriaException as e:
            raise e
        
        pprint(result)

        """pprint(object=(
            #res,
            ress
        ))"""
        """print(f"download status: {"готово" if download_status else "неудачно"}")"""
        """print(res)"""

if __name__ == "__main__":
    unittest.main()