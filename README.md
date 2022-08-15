## 1 Creacion de Entorno Virtual (EV)
- Uso Anaconda Prompt (anaconda3)
- cd Desktop
- cd fastapi-mongodb (carpeta creada para el proyecto)
- conda create --name fastapi-mongodb python=3 #creo EV y asigno python 3
- conda activate fastapi-mongodb               #activo el EV

## 2 Instalaciones de paquetes
- 1 pip install fastapi #instalar framework y todos los paquetes. 
- 2 pip install uvicorn #este paquete permite ejecutar app de fastapi
- 3 pip install pymongo #modulo para poder conectarnos a mongodb
- 4 pip install passlib #modulo para poder encriptar datos

## 3 Proyecto anotaciones
- uvicorn app:app #para ejecutar una app con uvicorn. app es el archivo py, y app es el objeto q devuelve FastAPI()
- uvicorn app:app --reload #cada vez qu guardo el proyecto automaticamente se refresca el server
- en folder routes la idea es tener rutas que permitan interactuar con la db, entonces @user.post se puede crear nuevos usuarios. Un @user.get('/users/{id}') puede usarse para obtener un unico usuario. Un @user.put('/users/{id}') puede usarse para actualizar un usuario. Un @user.delete('/users/{id}') se usa para eliminar un usuario segun id.
- FastAPI incluye una documentacion en Swagger que se va generando automaticamente y permite interactuar de forma practica con la API a medida que vamos progresando en el programa
- En la carpeta config se crea un archivo db.py para llamar una biblioteca de python (procedo a 2.3)
- El modelo que se crea para interactuar con la db se enontrará en la folder models. Importo pydantic
- Para encriptar datos uso passlib.hash import sha256_crypt. Luuego aplico sha256_crypt.encrypt para cifrar (ver 2.4)

# 4 base de datos
- 1 descargar mongodb local server
- 2 agregar la raiz de la carpeta bin al path  de windows
- 3 descargar mongo shell y copiar contenido de bin a nuetra raiz 
- 4 abrir como admin una ventana de cmd y ejecutar: mongod   para poder lanzar la db mongo
- 5 abrir otra ventana cmd y ejec: mongosh    para poder interactuar con la base de datos
- 6 ahora se puede insertar documentos a la coleccion 

