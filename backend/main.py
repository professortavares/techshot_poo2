from techshot.api import usuario
from fastapi import FastAPI

app = FastAPI()
app.include_router(usuario.router)