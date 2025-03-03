from fastapi.responses import JSONResponse
from src.common.enums import EnumHttpStatusCode
from typing import Any, Optional


class BaseResponse:
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

    def to_json(self) -> JSONResponse:
        return JSONResponse(content={"message": self.message}, status_code=self.status_code)


class SuccessResponse(BaseResponse):
    def __init__(self, data: Optional[Any] = None, message: str = "Success", status_code: int = EnumHttpStatusCode.HTTP_200.value):
        super().__init__(message=message, status_code=status_code)
        self.data = data

    def to_json(self) -> JSONResponse:
        return JSONResponse(content={"data": self.data, "message": self.message},
                            status_code=self.status_code)


class ErrorResponse(BaseResponse):
    def __init__(self, message: str, status_code: int = EnumHttpStatusCode.HTTP_400.value, details: Optional[Any] = None):
        super().__init__(message=message, status_code=status_code)
        self.details = details

    def to_json(self) -> JSONResponse:
        return JSONResponse(content={"message": self.message, "details": self.details},
                            status_code=self.status_code)
