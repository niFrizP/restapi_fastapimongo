from fastapi import FastAPI
from routes.usuario import usuario
from docs import tags_metadatos

app = FastAPI(
    title="REST API de Usuarios con FastAPI & MongoDB",
    description="esta es una API de usuarios con FastAPI y MongoDB ( ͡° ͜ʖ ͡°)",
    version="0.0.1 - Alpha",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    openapi_tags=tags_metadatos,
)
app.include_router(usuario)
