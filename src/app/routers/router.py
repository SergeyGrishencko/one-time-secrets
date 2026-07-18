from random import randint

from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["Генерация секретов"],
)


@router.post("/generate")
async def generate_secret(secret_message: str):
    """Эндпоинт, генерирующий секретный ключ."""
    secret_key = randint(0, 101)
    return secret_key


@router.get("/secrets/{secret_key}")
async def get_secret_message(secret_key: int):
    """Эндпоинт, возвращающий секретное слово по ключу."""
    return {"message": secret_key}
