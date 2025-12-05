from fastapi import FastAPI
import backend.routers.jugador

app = FastAPI(title="sigmotoa FC")

app.include_router(backend.routers.jugador.router)

@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}
