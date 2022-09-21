from typing import Callable


def hail_someone(name: str) -> str:
    return f'Hail to you, {name}'


def say_hi(name: str) -> str:
    return f'Hi, {name}'


def greetings(greet_func: Callable) -> str:
    return greet_func('Valera')


if __name__ == '__main__':
    print(greetings(hail_someone))
    # Hail to you, Valera
