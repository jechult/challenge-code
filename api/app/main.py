from fastapi import FastAPI
from routers import uploadfile, reporting, auth

app = FastAPI()

app.include_router(uploadfile.router)
app.include_router(reporting.router)
app.include_router(auth.router)