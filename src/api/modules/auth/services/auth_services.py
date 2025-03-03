
from ..repository.auth_repository import AuthRepository
from src.exceptions.user_exceptions import UserNotFound, InvalidPassword
from src.utils.user import check_password_hash
from src.utils.jwt import create_access_token

class AuthServices:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository

    def login(self, login_data: dict) -> dict:
        user = self.auth_repository.get_user_by_email(login_data["email"])
        if not user:
            raise UserNotFound("User not found")
        if not check_password_hash(user.password, login_data["password"]):
            raise InvalidPassword("Invalid password")
        return {"token": create_access_token(user.email)}