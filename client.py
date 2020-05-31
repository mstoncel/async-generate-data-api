import os
import aiohttp
from typing import Dict
from typedefs import StrOrURL


class Client:
    async def fetch(self, endpoint: StrOrURL, 
                    params: dict = {},
                    data: dict = {},
                    method='get',
                    ) -> Dict:
        base_url = 'https://randomuser.me/api/'
        client_data = {
            'headers': {'content-type': 'application/json'},
            'timeout': aiohttp.ClientTimeout(total=60) 
        }

        request_data = {
            'params': params,
            'data': data,
            'url': os.path.join(base_url, endpoint)
        }
        async with aiohttp.ClientSession(**client_data) as session:
            async with getattr(session, method)(**request_data) as resp:
                # TODO: Response error handle 
                return await resp.json()

    async def generate_user(self, gender, nat,*args, **kwargs):
        params = {
            'gender': gender,
            'nat': nat
        }
        response = await self.fetch(endpoint='', params=params)
        return response