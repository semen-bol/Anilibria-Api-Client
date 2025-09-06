import aiohttp

from typing import Dict, Any, Optional, Union
from urllib.parse import urlencode, urljoin, quote
from ..exceptions import AnilibriaValidationException, AnilibriaException


class AsyncBaseAPI:
    """
    Асинхронный базовый класс для работы с API.
    Предоставляет основные методы для отправки HTTP-запросов и работы с URL.
    """
    
    def __init__(
        self,
        base_url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 10,
    ):
        """
        Инициализация асинхронного API клиента.
        
        :param base_url: Базовый URL API
        :param headers: Заголовки по умолчанию для всех запросов
        :param timeout: Таймаут запросов в секундах
        """
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session: Optional[aiohttp.ClientSession] = None
        
    
    async def __aenter__(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()
            self._own_session = True
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._own_session and self._session:
            await self._session.close()
            self.session = None
            self._own_session = False
    
    async def _get_session(self) -> aiohttp.ClientSession:
        """Получить сессию, создавая новую если нужно"""
        if self.session is None:
            session = aiohttp.ClientSession()
            self.session = session
            self._own_session = True
        return self.session
    
    @staticmethod
    def build_query_string(params: Dict[str, Any]) -> str:
        """
        Создает query string из параметров.
        
        :param params: Словарь параметров
        :return: Строка вида ?key1=value1&key2=value2
        """
        if not params:
            return ""
        
        filtered_params = {k: v for k, v in params.items() if v is not None}
        if not filtered_params:
            return ""
        
        return "?" + urlencode(filtered_params, doseq=True)
    
    @staticmethod
    def build_url(base_url: str, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        """
        Строит полный URL с параметрами.
        
        :param base_url: Базовый URL
        :param endpoint: Конечная точка
        :param params: Параметры запроса
        :return: Полный URL с query-параметрами
        """

        url = urljoin(base_url + '/', endpoint.lstrip('/'))
        if params:
            url += AsyncBaseAPI.build_query_string(params)
        return url
    
    def encode_path_param(self, param: Any) -> str:
        """
        Кодирует параметр для использования в пути URL.
        
        :param param: Параметр для кодирования
        :return: Закодированная строка
        """

        return quote(str(param))
    
    def build_endpoint_with_params(self, endpoint_template: str, **path_params) -> str:
        """
        Строит endpoint с подставленными параметрами пути.
        
        :param endpoint_template: Шаблон endpoint (например: '/users/{user_id}/posts/{post_id}')
        :param path_params: Параметры для подстановки в путь
        :return: Готовый endpoint с подставленными параметрами
        """

        encoded_params = {k: self.encode_path_param(v) for k, v in path_params.items()}
        return endpoint_template.format(**encoded_params)
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Базовый метод для отправки HTTP-запросов.
        
        :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.)
        :param endpoint: Конечная точка API (относительный путь)
        :param params: Параметры запроса (для GET)
        :param data: Тело запроса (для POST, PUT)
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки запроса
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API (десериализованный JSON или сырые данные)
        :raises: HTTPError если статус ответа не 2xx
        """
        sees = await self._get_session()
        if not self.session or not sees:
            raise RuntimeError("Session not initialized. Use async with context manager.")
        
        url = self.build_url(self.base_url, endpoint, params)
        request_headers = {**self.headers, **(headers or {})}
        
        try:
            async with self.session.request(
                method=method,
                url=url,
                data=data,
                json=json_data,
                headers=request_headers,
                **kwargs
            ) as response:
                if response.status == 422:
                    error_data = await response.json()
                    if error_data.get("errors"):
                        raise AnilibriaValidationException(error_data)
                    else:
                        raise AnilibriaValidationException({"error": "Ошибка валидации входных параметров"})    

                response.raise_for_status()
                
                content_type = response.headers.get('Content-Type', '')
                if 'application/json' in content_type:
                    return await response.json()
                elif 'application/x-bittorrent' in content_type:
                    return await response.read()
                
                return await response.text()
                
        except aiohttp.ClientError as e:
            raise self._handle_error(e)
        
        finally:
            if self._own_session and self.session:
                await self.session.close()
                self.session = None
                self._own_session = False
    
    def _handle_error(self, error: aiohttp.ClientError) -> Exception:
        """
        Обработка ошибок запроса.
        
        :param error: Исключение aiohttp
        :return: Исключение для проброса
        """

        if hasattr(error, 'errors'):
            return error
        return AnilibriaException(error)
    
    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Отправка GET запроса.
        
        :param endpoint: Конечная точка API
        :param params: Параметры запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request('GET', endpoint, params=params, headers=headers, **kwargs)
    
    async def post(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Отправка POST запроса.
        
        :param endpoint: Конечная точка API
        :param data: Тело запроса
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request('POST', endpoint, data=data, json_data=json_data, headers=headers, **kwargs)
    
    async def put(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Отправка PUT запроса.
        
        :param endpoint: Конечная точка API
        :param data: Тело запроса
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request('PUT', endpoint, data=data, json_data=json_data, headers=headers, **kwargs)
    
    async def delete(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Отправка DELETE запроса.
        
        :param endpoint: Конечная точка API
        :param headers: Дополнительные заголовки
        :param json_data: JSON тело запроса
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request('DELETE', endpoint, json_data=json_data, headers=headers, **kwargs)
    
    async def patch(
        self,
        endpoint: str,
        data: Optional[Union[Dict[str, Any], str, bytes]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> Union[Dict[str, Any], str, bytes]:
        """
        Отправка PATCH запроса.
        
        :param endpoint: Конечная точка API
        :param data: Тело запроса
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request('PATCH', endpoint, data=data, json_data=json_data, headers=headers, **kwargs)