import string
import random


class TokenGenerator(object):

    symbols = string.ascii_letters + string.digits

    @classmethod
    def generate(cls, length):
        return "".join(
            [random.choice(cls.symbols) for _ in range(length)]
        )
