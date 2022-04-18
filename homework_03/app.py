from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """
    "GET /"
    """
    return {"message": "Hello World!"}

@app.get("/add")
def add(a: int, b: int):
    """

    :param a:
    :param b:
    :return:
    """
    return {"a": a, "b": b, "sum": a + b}