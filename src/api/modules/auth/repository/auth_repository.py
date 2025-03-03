from src.utils.db import prisma

class AuthRepository:
    def __init__(self):
        self.db = prisma.get_client()
        
    def get_user_by_email(self, email: str):
        return self.db.user.find_first(where={"email": email})