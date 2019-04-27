import string
import random


class TokenGenerator(object):
    """
    Класс для генерации токенов
    """

    symbols = string.ascii_letters + string.digits
    """Набор символов из которых будет сгенерирована псевдослучайная строка"""

    @classmethod
    def generate(cls, length):
        """
        Метод генерации псевдослучайно строки

        :param length: длина строки

        """
        return "".join(
            [random.choice(cls.symbols) for _ in range(length)]
        )
