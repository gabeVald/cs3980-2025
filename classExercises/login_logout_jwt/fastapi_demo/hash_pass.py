#pip install passlib[bcyrpt]
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])

class HashPassword:
    #Not needed in ultimate use
    def create_hash(self, password:str):
        return pwd_context.hash(password)
    #hashed_pass is the password we'd retrieve from the db that corresponds to username they enter
    def verify_hash(self, input_password:str, hashed_password:str):
        return pwd_context.verify(input_password, hashed_password)