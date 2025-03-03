import uvicorn
from src.common.constants import API_PREFIX, API_VERSION, API_TITLE, API_DESCRIPTION, CORS_ALLOWED_ORIGINS, CORS_ALLOWED_CREDENTIALS, CORS_ALLOWED_METHODS, CORS_ALLOWED_HEADERS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.utils.db import connect_db, disconnect_db
from src.routes.index_routes import router as index_router
from src.utils.errors.http_error_handlers import HttpErrorHandler


@asynccontextmanager
async def db_session(app: FastAPI):
    await connect_db()
    try:
        yield
    finally:
        await disconnect_db()


app = FastAPI(
    lifespan=db_session,
    description=f'{API_DESCRIPTION}',
    title=f'{API_TITLE}',
    version=f'{API_VERSION}',
    root_path=f'{API_PREFIX}/{API_VERSION}',
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

#middleware
app.add_middleware(HttpErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ALLOWED_ORIGINS],
    allow_credentials=CORS_ALLOWED_CREDENTIALS,
    allow_methods=[CORS_ALLOWED_METHODS],
    allow_headers=[CORS_ALLOWED_HEADERS]
)


# routes
@app.get("/")
async def read_root():
    return {
        "title": f"{API_TITLE}",
        "description": f"{API_DESCRIPTION}",
        "docs": f"{API_PREFIX}/{API_VERSION}/docs",
        "redoc": f"{API_PREFIX}/{API_VERSION}/redoc"
    }


app.include_router(prefix=f'{API_PREFIX}/{API_VERSION}', router=index_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
