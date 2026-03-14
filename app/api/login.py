from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import create_access_token, pwd_context
from app.services import user_service
from app.schemas.error_schema import ErrorResponse

router = APIRouter(tags=["Authentication"])

@router.post(
    "/login",
    responses={
        400: {"model": ErrorResponse, "description": "Invalid credentials"},
    }
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login using username and password"""
    user = user_service.get_login_user(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["pw"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": form_data.username, "role": user["role"]})
    return {"access_token": token, "token_type": "Bearer"}