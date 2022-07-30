from fastapi import FastAPI
from routers import uploadfile

app = FastAPI()

app.include_router(uploadfile.router)