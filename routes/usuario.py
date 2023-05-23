from fastapi import APIRouter, Response, status, HTTPException
from config.db import conx
from schemas.usuario import entidadUsuario, entidadUsuarios
from models.usuario import Usuario
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

usuario = APIRouter()


@usuario.get('/usuarios', response_model=list[Usuario], tags=["Usuarios"])
def buscar_usuarios():
    return entidadUsuarios(conx.local.usuario.find())


@usuario.post('/usuarios', response_model=Usuario, tags=["Usuarios"])
def crear_usuario(usuario: Usuario):
    nuevo_usuario = dict(usuario)
    nuevo_usuario["password"] = sha256_crypt.encrypt(nuevo_usuario["password"])
    del nuevo_usuario["id"]

    id = conx.local.usuario.insert_one(nuevo_usuario).inserted_id
    usuario = conx.local.usuario.find_one({"_id": id})
    return entidadUsuario(usuario)


@usuario.get('/usuarios/{id}', response_model=Usuario, tags=["Usuarios"])
def buscar_usuario(id: str):
    print(id)
    return entidadUsuario(conx.local.usuario.find_one({"_id": ObjectId(id)}))


@usuario.put('/usuarios/{id}', response_model=Usuario, tags=["Usuarios"])
def actualizar_usuario(id: str, usuario: Usuario):
    conx.local.usuario.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(usuario)}
    )
    return entidadUsuario(conx.local.usuario.find_one({"_id": ObjectId(id)}))


@usuario.delete('/usuarios/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def borrar_usuario(id: str):
    entidadUsuario(conx.local.usuario.find_one_and_delete({"_id": ObjectId(id)}))
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        entidadUsuario(usuario)
    return Response(status_code=HTTP_204_NO_CONTENT)
