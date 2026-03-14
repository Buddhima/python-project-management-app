from datetime import datetime, timedelta
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.schemas.user_schema import LoginUser

SECRET_KEY = "supersecretkey" # This should go into a secure vault (eg: HashiCorp Vault, AWS Secrets Manager)
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return LoginUser(username=payload.get("sub"), role=payload.get("role"))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

class RoleChecker:
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: LoginUser = Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return user