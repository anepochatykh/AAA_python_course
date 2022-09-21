from typing import Callable


def oops_decorator(func: Callable) -> Callable:
    def wrapper():
        print('I say oops')
        func()
        print('I say oops again')
    return wrapper


@oops_decorator
def say_hello_world() -> str:
    print('Hello world')


if __name__ == '__main__':
    say_hello_world()
