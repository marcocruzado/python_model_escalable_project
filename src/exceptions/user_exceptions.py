from src.common.enums import EnumHttpStatusCode
from src.common.responses import ErrorResponse

class UserNotFound(ErrorResponse):
    def __init__(self, message: str = "User not found"):
        super().__init__(message=message, status_code=EnumHttpStatusCode.HTTP_404.value)

class InvalidPassword(ErrorResponse):
    def __init__(self, message: str = "Invalid password"):
        super().__init__(message=message, status_code=EnumHttpStatusCode.HTTP_400.value)
