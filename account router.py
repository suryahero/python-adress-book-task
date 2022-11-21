from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
import db
from . import schema
from . import services
from . import validator

from . jwt import create_access_token, get_current_user

import db
from . import hashing
from . models import Account

router = APIRouter(tags=['Accounts'], prefix='/account')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.Account,
                                   database: Session = Depends(db.get_db)):

    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail="This user with this email already exists in the system."
        )

    new_user = await services.new_user_register(request, database)
    return new_user


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),
          database: Session = Depends(db.get_db)):
    user = database.query(Account).filter(Account.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials throw")

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")

    # Generate a JWT Token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/', response_model=List[schema.DisplayAccount])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.all_users(database)


@router.get('/profile', response_model=schema.DisplayAccount)
async def get_profile(database: Session = Depends(db.get_db), current_user: schema.Account = Depends(get_current_user)):
    return await services.get_profile(database, current_user)


@router.get('/{user_id}', response_model=schema.DisplayAccount)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)







