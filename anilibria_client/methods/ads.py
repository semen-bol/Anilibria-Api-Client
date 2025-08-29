from ._libria import BaseMethod


class AdsMethod(BaseMethod):
    async def vasts(
            self
    ):
        """
        Возвращает список со всеми доступными для использования VAST кампаниями
        """
        return await self._api.get("/ads/vasts")
    
    async def vasts_chain(
            self
    ):
        """
        Возвращает XML страницу со всеми доступными для использования VAST кампаниями
        """
        headers = {
            "Content-Type": "application/xml"
        }

        return await self._api.get("/ads/vasts/chain", headers=headers)