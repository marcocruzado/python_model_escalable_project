class TokenExpired(Exception):
    def __init__(self, message: str = "Token has expired", status_code: int = 401):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        
class TokenInvalid(Exception):
    def __init__(self, message: str = "Token is invalid", status_code: int = 401):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
