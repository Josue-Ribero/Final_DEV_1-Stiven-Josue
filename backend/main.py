from fastapi import FastAPI, Request, UploadFile, File
from .routers import jugador_router
from .db.db import createAllTables

app = FastAPI(title="sigmotoa FC", lifespan=createAllTables)

# Routers de la app
from .routers import (
    jugador_router,
    estadisticas_router,
    partido_router
)

# Inclusion de los routers en la app
routers = [
    jugador_router.router,
    estadisticas_router.router,
    partido_router.router
]

# Incluir los routers en la app
for router in routers:
    app.include_router(router)


# Imagenes
@app.post("/bucket")
async def subirImagen(archivo: UploadFile = File(...)):
    from .utils.bucket import cargarArchivo
    resultado = await cargarArchivo(archivo)
    return resultado

# Inicialización de la app base
@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}
