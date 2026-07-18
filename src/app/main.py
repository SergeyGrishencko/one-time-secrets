from fastapi import FastAPI

from src.app.routers.router import router

app = FastAPI(title="Сервис для генерации одноразовых секретов")

app.include_router(router)


@app.get("/echo")
async def get_information(message: str):
    """Транслирует сообщение от пользователя."""
    return message
