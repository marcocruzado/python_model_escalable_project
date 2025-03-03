
from ..services.auth_services import AuthServices


class AuthController():
    def __init__(self, auth_service: AuthServices):
        self.auth_service = auth_service

    async def login(self):
        try:
            response = self.auth_service.login()
            return response
        except Exception as e:
            return str(e)