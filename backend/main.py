from techshot.api.usuario import UsuarioApi
from fastapi import FastAPI

app = FastAPI()
api_usuario = UsuarioApi()
app.include_router(app.router)
