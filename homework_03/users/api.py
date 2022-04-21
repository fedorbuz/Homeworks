from fastapi import APIRouter

from . import crud
from . schemas import UserIn, UserOut
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut])
def list_users():
    return crud.list_users()


@router.post("", response_model=UserOut)
def create_user(user_in: UserIn):
    return crud.create_user(user_in)