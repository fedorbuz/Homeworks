#docker run -it -p 8001:8000 app

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/")
def ping():


    return {"message": "pong"}


