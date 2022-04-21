from .schemas import User, UserIn

USER_TO_USER: dict[str, User] = {}


def list_users() -> list[User]:
    return list(USER_TO_USER.values())


def create_user(user_in: UserIn) -> User:
    new_id = len(USER_TO_USER) + 1
    user = User(id=new_id, **user_in.dict())
    USER_TO_USER[new_id] = user
    return user