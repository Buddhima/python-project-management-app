from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    MANAGER = "manager"
    STAFF = "staff"

class LoginUser(BaseModel):
    username: str
    role: UserRole