from secrets import choice
from string import ascii_letters, digits

LENGTH_KEY = 64
ALPHABET_ASCII = ascii_letters + digits


class SecretsRepository:
    """Класс для операций над секретами."""

    @classmethod
    async def generate_secret_key(cls):
        """Генерирует уникальный ключ из ASCII символов.

        ALPHABET_ASCII: Набор допустимых символов в коде ASCII
        LENGTH_KEY: Длина генерируемого ключа
        """

        return "".join(choice(ALPHABET_ASCII) for _ in range(LENGTH_KEY))
