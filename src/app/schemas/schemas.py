from pydantic import BaseModel


class BaseSecretMessage(BaseModel):
    """Базовая схема для секретной фразы."""

    secret_message: str


class GenerateSecretsRequest(BaseSecretMessage):
    """Схема запроса эндпоинта `/api/generate`."""


class SecretMessageResponse(BaseSecretMessage):
    """Схема ответа эндпоинта `/api/secrets/{secret_key}`."""
