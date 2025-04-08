from datetime import datetime, timedelta, timezone
import jwt

from token_data import TokenData
#generated from: openssl rand -hex 32
SECRET_KEY = "93f6dcefd4a735545cdbc546e3236a8f3cbf5e0fbe6702702eb84b6086a35e9e"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    payload = data.copy()
    #if we have anything for expires_delta, set the expire time to be now + delta
    expire = datetime.now(timezone.utc) + expires_delta
    payload.update({"exp": expire })
    encoded = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

def decode_jwt_token(token: str) -> TokenData|None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str=payload.get("username")
        exp: int=payload.get("exp")
        return TokenData(username= username, exp_datetime= datetime.fromtimestamp(exp))
    except jwt.InvalidTokenError: 
        print("Invalid JWT Token.")
    
    

a = create_access_token({"username": "gmvald"})
print(a)

b = decode_jwt_token(a)

print(b.username)
print(b.exp_datetime)