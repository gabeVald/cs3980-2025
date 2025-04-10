from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from hash_pass import HashPassword
from auth import Token, TokenData, create_access_token, decode_jwt_token

in_memory_db = [
    {
    "username": "hi", 
    "password":"$2b$12$sX0tOyspKqQd.1e/usfcu.eknSScBXgbBk0qLUxedWo1/i/LjuDM6"
    }
]

app = FastAPI()
hash_password = HashPassword()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") #Points to /token below

def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    #Authenticate user by verifying the user exists in DB
    username = form_data.username
    #This would need to hit the mondoDB when not using in memory db
    for u in in_memory_db:
        if u["username"] == username:
            print(u["password"]) #This is showing the user's hashed password we'll compare their entered pass to
            #print(hash_password.create_hash("hi123")) #This simulates the registry process so we have a hashed pass to compare with
            authenticated = hash_password.verify_hash(form_data.password, u["password"]) #u["password"] is what we'd get hashed from the db
            if authenticated:
                access_token = create_access_token({"username": username})
                return Token(access_token=access_token)
    return HTTPException(status_code=401, detail="Invalid Username or Password")

@app.get("/users/me")
async def read_my_username(user: Annotated[TokenData, Depends(get_user)]) -> TokenData:
    return user