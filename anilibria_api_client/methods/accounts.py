from ._libria import BaseMethod
from ..models import TimeCode, ReleaseCollection
from ._helper import validate_collection, validated_json_collection
from typing import Optional, List


class AccountsMethod(BaseMethod):
    async def otp_get(
            self, 
            device_id: str
        ):
        """
        Запрашиваем новый одноразовый пароль

        :param device_id: ID девайса (необходим)
        """

        data = {
            'device_id': device_id
        }

        return await self._api.post("/accounts/otp/get", json_data=data)
    
    async def otp_accept(
            self, 
            code: int        
        ):
        """
        Присоединяем пользователя к выданному одноразовому паролю

        :param code: Код девайса (необходим)
        """

        data = {
            'code': code
        }

        return await self._api.post("/accounts/otp/accept", json_data=data)
    
    async def otp_login(
            self, 
            code: int,
            device_id: str
        ):
        """
        Авторизуемся по выданному одноразовому паролю

        :param code: Код девайса (необходим)
        :param device_id: ID девайса (необходим)
        """

        data = {
            'code': code,
            'device_id': device_id
        }

        return await self._api.post("/accounts/otp/login", json_data=data)
    
    async def users_auth_login(
            self,
            login: str,
            password: str,
    ):
        """
        Авторизация пользователя по логину и паролю. Создание сессии пользователя, выдача токена авторизации для использования в cookies или в Bearer Token

        :param login: Логин аккаунта (необходим)
        :param password: Пароль аккаунта (необходим)
        """

        data = {
            "login": login,
            "password": password
        }

        return await self._api.post("/accounts/users/auth/login", json_data=data)
    
    async def users_auth_logout(
            self
    ):
        """
        Деавторизовать пользователя
        """
        return await self._api.post("/accounts/users/auth/login")
    
    async def users_auth_social_login(
            self,
            provider: str,
    ):
        """
        Позволяет авторизовать пользователя через некоторые социальные сети

        :param provider: Провайдер социальной сети vk, google, patreon, discord (необходим)
        """
        return await self._api.get(f"/accounts/users/auth/social/{provider}/login")
    
    async def users_auth_social_authenticate(
            self,
            state: str
    ):
        """
        Позволяет аутентифицировать авторизованного через социальную сеть пользователя

        :param state: Ключ аутентификации users_auth_social_login (необходим)
        """
        query = {
            "state": state
        }

        return await self._api.get("/accounts/users/auth/social/authenticate", params=query)
    
    async def users_auth_password_forget(
            self,
            email: str
    ): 
        """
        Отправление ссылки на восстановление забытого пароля

        :param email: Email аккаунта
        """

        data = {
            "email": email
        }

        return await self._api.post("/accounts/users/auth/password/forget", json_data=data)
    
    async def users_auth_password_reset(
            self,
            token: str,
            password: str,
            password_confirmation: str
    ): 
        """
        Сброс и установка нового пароля
        
        :param token: Токен с email
        :param password: Пароль
        :param password_confirmation: Подтверждение пароля
        """

        data = {
            "token": token,
            "password": password,
            "password_confirmation": password_confirmation
        }

        return await self._api.post("/accounts/users/auth/password/reset", json_data=data)
    
    async def users_me_collections_references_age_ratings(
            self
    ):
        """
        Возвращает список возрастных рейтингов в коллекциях текущего пользователя (auth need)
        """

        return await self._api.get("/accounts/users/me/collections/references/age-ratings")
    
    async def users_me_collections_references_genres(
            self
    ):
        """
        Возвращает список жанров в коллекциях текущего пользователя (auth need)
        """

        return await self._api.get("/accounts/users/me/collections/references/genres")
    
    async def users_me_collections_references_types(
            self
    ):
        """
        Возвращает список типов в коллекциях текущего пользователя (auth need)
        """

        return await self._api.get("/accounts/users/me/collections/references/types")
    
    async def users_me_collections_references_years(
            self
    ):
        """
        Возвращает список годов в коллекциях текущего пользователя (auth need)
        """

        return await self._api.get("/accounts/users/me/collections/references/years")
    
    async def users_me_collections_ids(
            self      
    ):
        """
        Возвращает данные по идентификаторам релизов и типов коллекций авторизованного пользователя
        """
        return await self._api.get("/accounts/users/me/collections/ids")
    
    async def users_me_collections_releases_get(
            self, 
            release_collection: ReleaseCollection
        ):
            """
            Возвращает данные по релизам из определенной коллекции авторизованного пользователя
            
            :param release_collection: тело ReleaseCollection
            """
            params = {
                'page': release_collection.page,
                'limit': release_collection.limit,
                'type_of_collection': release_collection.type_of_collection.value,
                'include': release_collection.include,
                'exclude': release_collection.exclude
            }
            
            coll = await validate_collection(params=release_collection)
            final_params = {**params, **coll}
            
            return await self._api.get("/accounts/users/me/collections/releases", params=final_params)
    
    async def users_me_collections_releases_post(
            self, 
            release_collection: ReleaseCollection
        ):
            """
            Возвращает данные по релизам из определенной коллекции авторизованного пользователя
            
            :param release_collection: тело ReleaseCollection
            """
            json = {
                'page': release_collection.page,
                'limit': release_collection.limit,
                'type_of_collection': release_collection.type_of_collection.value,
                'include': release_collection.include,
                'exclude': release_collection.exclude
            }
            
            coll = await validated_json_collection(release=release_collection)
            final_json = {**json, **coll}

            return await self._api.post("/accounts/users/me/collections/releases", json_data=final_json)
    
    async def users_me_collections_add(
            self, 
            release_ids: List[int]
    ):
        """
        Добавляет релизы в избранное авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        return await self._api.post("/accounts/users/me/favorites", json_data=params)

    async def users_me_collections_delete(
            self, 
            release_ids: List[int]
    ):
        """
        Удаляет релизы из избранного авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        return await self._api.delete("/accounts/users/me/favorites", json_data=params)
    
    async def users_me_profile(
            self, 
            include: Optional[str] = None, 
            exclude: Optional[str] = None
    ):
        """
        Возвращает данные профиля авторизованного пользователя (auth need)

        :param include: Опционально. Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Example : id,type.genres
        :param exclude: Опционально. Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include Example : poster,description
        """

        query = {
            'include': include,
            'exclude': exclude
        }

        return await self._api.get("/accounts/users/me/profile", params=query)
    
    async def users_me_views_history(
            self,
            page: Optional[int] = None,
            limit: Optional[int] = None,
            include: Optional[str] = None,
            exclude: Optional[str] = None
    ):
        """
        Возвращает историю просмотров эпизодов авторизованного пользователя

        :param page: Опционально. Номер страницы
        :param limit: Опционально. Лимит на страницу
        :param include: Опционально. Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
        :param exclude: Опционально. Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
        """
        params = {
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude
        }
        return await self._api.get("/accounts/users/me/views/history", params=params)

    async def users_me_views_timecodes(
            self,
            since: Optional[str]
    ):
        """
        Возвращает таймкоды по прогрессу просмотренных эпизодов
        
        :param since: Опционально. Возвращает только таймкоды, которые были добавлены после указанного времени (в iso формате). Example: 2025-05-12T07:20:50.52Z
        """
        params = {
            "since": since
        }
        return await self._api.get("/accounts/users/me/views/timecodes", params=params)

    async def users_me_views_timecodes_update(
            self,
            timecode_list: List[TimeCode]
    ):
        """
        Обновляет таймкоды просмотренных эпизодов

        :param timecode_list: Лист из обьектов TimeCode. Example: [TimeCode(...)]
        """
        json = [timecode.model_dump(mode='json') for timecode in timecode_list]
        
        return await self._api.post("/accounts/users/me/views/timecodes", json_data=json)
    
    async def users_me_views_timecodes_delete(
            self,
            episode_id_list: List[str]
    ):
        """
        Удаляет данные по таймкодам просмотров для указанных эпизодов
        
        :param episode_id_list: Лист из episode_id. Example: ["id", "id"]
        """
        list_ = []
        for episode in episode_id_list:
            list_.append({"release_episode_id": episode})

        return await self._api.delete("/accounts/users/me/views/timecodes", json_data=list_)