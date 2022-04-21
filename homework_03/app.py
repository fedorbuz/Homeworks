from fastapi import FastAPI
from pydantic import constr

from items_views import router as items_router
from users.api import router as users_router
app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

@app.get("/")
def root():
    """
    "GET /"
    """
    return {"message": "Hello World!"}

@app.get("/hello")
# hello_view(name: str = "King"):
def hello_view(name: constr(min_length=3) = "King"):
    """
    GET /hello?name=King
    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    """

    :param a:
    :param b:
    :return:
    """
    return {"a": a, "b": b, "sum": a + b}