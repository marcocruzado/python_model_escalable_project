
from ..services.auth_services import AuthServices


class AuthController():
    def __init__(self, auth_service: AuthServices):
        self.auth_service = auth_service

    async def get_users(self):
        try:
            response = {
                "message": "Hello, World",
                "data": []
            }
            return response
        except Exception as e:
            return str(e)