def entidadUsuario(item) -> dict:
    return{
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "email": item["email"],
        "password": item["password"]
    }

def entidadUsuarios(entidad) -> list:
    return [entidadUsuario(item) for item in entidad]