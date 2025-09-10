from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
services = {}

class Service(BaseModel):
    name: str
    port: int

@app.get('/index')
def index():
    return services

@app.post('/register')
def register(service: Service):
    name = service.name
    port = service.port
    services[name] = f"localhost:{port}"
    return {"message": f"Serviço '{name}' registrado em localhost:{port}"}

@app.get('/discover/{name}')
def discover(name: str):
    address = services.get(name)
    if address:
        return {"address": address}
    raise HTTPException(status_code=404, detail="Serviço não encontrado.")