import os
import aiohttp
from typing import Dict

class Client:
    async def fetch(self, endpoint: str, 
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

    async def generate_user(self, *args, **kwargs):
        params = {
            'gender': kwargs.get('gender'),
            'nat': kwargs.get('nat'),
            'results': kwargs.get('results')
        }
        clean_data = { key: value for key, value in params.items() if value is not None}
        response = await self.fetch(endpoint='', params=clean_data)
        return response