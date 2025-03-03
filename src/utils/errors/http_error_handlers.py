
from fastapi import FastAPI
from src.common.enums import EnumHttpStatusCode
from starlette.middleware.base import BaseHTTPMiddleware
import fastapi.requests as Requests
from fastapi.responses import Response, JSONResponse

class HttpErrorHandler(BaseHTTPMiddleware):
    
    def __init__(self, app:FastAPI):
        super().__init__(app)
        
    async def dispatch(self, request: Requests, call_next) -> Response | JSONResponse:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            content = {"message": str(e)}
            status_code = EnumHttpStatusCode.HTTP_500
            return JSONResponse(content=content, status_code=status_code)