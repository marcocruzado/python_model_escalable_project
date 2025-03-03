from src.common.enums import EnumHttpStatusCode
from src.common.responses import ErrorResponse

class TokenExpired(Exception):
    def __init__(self, message: str = "Token has expired"):
        self.message = message
        super().__init__(self.message)
        
class TokenInvalid(Exception):
    def __init__(self, message: str = "Token is invalid"):
        self.message = message
        super().__init__(self.message)
