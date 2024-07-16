from fastapi import FastAPI
from app.routers import init_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

init_app(app)

# Configuração básica para permitir todos os origens (todos os domínios) com todos os métodos e cabeçalhos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos os origens (todos os domínios)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)
