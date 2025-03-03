import os
import dotenv


dotenv.load_dotenv()

# Constants variables
DATABASE_URL = os.getenv('DATABASE_URL', 'db.sqlite3')
API_HOST = os.getenv('API_HOST', '127.0.0.1')
API_VERSION = os.getenv('API_VERSION', 'v1')
API_PREFIX = os.getenv('API_PREFIX', '/api')
API_TITLE = os.getenv('API_TITLE', 'FastAPI')
API_DESCRIPTION = os.getenv('API_DESCRIPTION', 'FastAPI template')


CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '*')
CORS_ALLOWED_METHODS = os.getenv('CORS_ALLOWED_METHODS', 'GET, POST, PUT, DELETE, OPTIONS')
CORS_ALLOWED_HEADERS = os.getenv('CORS_ALLOWED_HEADERS', '*')
CORS_ALLOWED_CREDENTIALS = os.getenv('CORS_ALLOW_CREDENTIALS', True)

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_EXPIRE_MINUTES = os.getenv('JWT_EXPIRE_MINUTES', 60)
