from client import Client

class Adapter:
    async def generate_user(self, params, *args, **kwargs):
        response = await Client().generate_user(**params)
        return response
