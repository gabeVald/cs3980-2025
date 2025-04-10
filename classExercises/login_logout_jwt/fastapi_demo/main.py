from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import Token, TokenData, create_access_token, decode_jwt_token

in_memory_db = [
    {"username": "hi", "password":""}
]

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") #Points to /token below

def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    #Assume that the user is authenticated by username and password
    username = form_data.username
    access_token = create_access_token({"username": username})
    return Token(access_token=access_token)

@app.get("/users/me")
async def read_my_username(user: Annotated[TokenData, Depends(get_user)]) -> TokenData:
    return user