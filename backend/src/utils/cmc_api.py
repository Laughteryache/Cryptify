from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
params = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'eec48b79-70c8-4d08-800f-350750cadd7d'
}


session = Session()
session.headers.update(headers)


try:
    response = session.get(url=url,
                           params=params)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

