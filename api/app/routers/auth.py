from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from oatuh2 import create_access_token

# just for testing login request
USER = 'jechult'
PASSWORD = 'admin'

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    
    if user_credentials.username != USER or user_credentials.password != PASSWORD:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = 'Invalid credentials'
        )
    
    access_token = create_access_token(data = {"user_id": user_credentials.username})
    
    return {'access_token': access_token, "token_type": "bearer"}