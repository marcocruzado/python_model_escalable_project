from fastapi import APIRouter
from src.api.modules.auth.routes.auth_router import auth_router

router = APIRouter()

router.include_router(prefix="/auth", router=auth_router)