from random import randint

from fastapi import APIRouter

from src.app.repository.secrets import SecretsRepository
from src.app.schemas.schemas import GenerateSecretsRequest, SecretMessageResponse

router = APIRouter(
    prefix="/api",
    tags=["Генерация секретов"],
)


@router.post("/generate")
async def generate_secret(secret_message: GenerateSecretsRequest):
    """Эндпоинт, генерирующий секретный ключ."""
    secret_key = await SecretsRepository.generate_secret_key()
    return secret_key


@router.get("/secrets/{secret_key}")
async def get_secret_message(secret_key: str):
    """Эндпоинт, возвращающий секретное слово по ключу."""
    return SecretMessageResponse(secret_message="Hello, World!")
