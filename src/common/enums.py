from enum import Enum


class EnumHttpMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    
class EnumHttpStatusCode(Enum):
    HTTP_200 = 200
    HTTP_201 = 201
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_500 = 500
    HTTP_501 = 501
    HTTP_502 = 502
    HTTP_503 = 503