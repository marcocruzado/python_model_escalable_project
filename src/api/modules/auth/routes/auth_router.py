from fastapi import APIRouter, HTTPException
from ..controllers.aurh_controllers import AuthController

auth_router = APIRouter(tags=["Auth"])


@auth_router.get("/")
async def get_users():
    try:
        response = AuthController.get_users()
        return HTTPException(status_code=200, detail=response)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
