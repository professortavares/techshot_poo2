from techshot.api import ApiUsuario
from fastapi import FastAPI

app = FastAPI()
api_usuario = ApiUsuario()
app.include_router(api_usuario.router)