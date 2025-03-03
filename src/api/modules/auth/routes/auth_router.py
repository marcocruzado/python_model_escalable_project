from fastapi import APIRouter, HTTPException
from ..controllers.auth_controllers import AuthController

auth_router = APIRouter(tags=["Auth"])

@auth_router.get("/login")
async def login():
    try:
        response = AuthController.login()
        return response  # Devolver directamente la respuesta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
