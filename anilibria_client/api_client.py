from .api_class import AsyncBaseAPI
from typing import Optional

from .methods import (
    AccountsMethod
)

class AsyncAnilibriaAPI(AsyncBaseAPI):
    """
    Асинхронный клиент для работы с AnilibriaAPI
    """
    def __init__(
            self,
            base_url: str = "https://anilibria.top/api/v1",
            authorization: str = "Bearer" # Получить с помощью accounts.users_auth_login() 
        ):
        headers = {
            "Content-Type": "application/json",
            "Authorization": authorization
        }
        super().__init__(base_url=base_url, headers=headers)
        self.accounts = AccountsMethod(api=self)

    