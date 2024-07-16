from aiohttp import ClientSession
from src.config import settings

base_url = 'https://pro-api.coinmarketcap.com'


class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': api_key,
            }
        )


class CMCHTTPClient(HTTPClient):
    async def get_listings(self):
        async with self._session.get('/v1/cryptocurrency/listings/latest?limit=10') as response:
            result = await response.json()
            return result['data']
        
    async def get_currency(self, currency_id: int):
        async with self._session.get('/v2/cryptocurrency/quotes/latest',
                                     params={'id': currency_id}) as response:
            result = await response.json()
            return result["data"][str(currency_id)]


cmc_client = CMCHTTPClient(base_url=base_url,
                           api_key=settings.API_KEY)