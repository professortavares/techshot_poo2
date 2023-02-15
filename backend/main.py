from techshot.api import usuario
from techshot.api import postagem
from fastapi import FastAPI


app = FastAPI()
app.include_router(usuario.router, prefix="/usuarios")
app.include_router(postagem.router, prefix="/postagens")