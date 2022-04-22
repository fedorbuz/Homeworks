from .schemas import User, UserIn
from typing import Optional

USER_TO_USER: dict[str, User] = {}
USER_TO_TOKEN: dict[str, User] = {}

def list_users() -> list[User]:
    return list(USER_TO_USER.values())


def create_user(user_in: UserIn) -> User:
    new_id = len(USER_TO_USER) + 1
    user = User(id=new_id, **user_in.dict())
    USER_TO_USER[new_id] = user
    USER_TO_TOKEN[user.token] = user

    return user


def get_user(user_id) -> Optional[User]:
    return USER_TO_USER.get(user_id)


def get_user_by_token(token: str) -> Optional[User]:
    return USER_TO_TOKEN.get(token)