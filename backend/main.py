from techshot.api.usuario import UsuarioApi
from fastapi import FastAPI

app = FastAPI()
app.include_router(UsuarioApi().router)
