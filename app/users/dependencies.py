from datetime import datetime, timezone
from jose import jwt, JWTError

from fastapi import Depends, Request

from app.config import settings
from app.users.dao import UsersDAO
from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotExistException,
)


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    
    try:
        payload = jwt.decode(
        token, settings.SECRET_KEY, settings.ALGORITHM
        )

    except JWTError:
        raise IncorrectTokenFormatException
        
    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.now(tz=timezone.utc).timestamp()):
        raise TokenExpiredException
    
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotExistException
    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotExistException
        
    return user
    