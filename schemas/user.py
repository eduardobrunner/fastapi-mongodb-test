#son los esquemas dedicados a los usuarios
# sirven para describir que va a tener cada usuario

def userEntity(item) -> dict: #cuando llame a userEntity me devuelve un diccionario
                              # con los mismos datos que estoy recibiendo
    return{
        "id": item["id"],
        "name": item["name"],
        "email": item ["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:
    [userEntity(item) for item in entity] #recorro la lista, por cada elemento "item", por cada elemento 
                                          #que estoy recorriendo le voy a dar ese elemento a userEntity pa que
                                          #genere el esquema que armamos mas arriba