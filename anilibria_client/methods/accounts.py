from ._libria import BaseMethod
from typing import Optional

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
    
    async def otp_accept(
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
            'code': code
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
    
    async def users_me_profile(
            self, 
            include: Optional[str] = None, 
            exclude: Optional[str] = None
    ):
        """
        Возвращает данные профиля авторизованного пользователя

        :param include: Опционально. Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Example : id,type.genres
        :param exclude: Опционально. Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include Example : poster,description
        """

        query = {
            'include': include,
            'exclude': exclude
        }

        return await self._api.get("/accounts/users/me/profile", params=query)

    