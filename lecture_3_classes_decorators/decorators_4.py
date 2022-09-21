from typing import Callable


# идея применения декораторов
def oops_decorator(func: Callable) -> Callable:
    def wrapper():
        print('I say oops')
        func()
        print('I say oops again')
    return wrapper


def say_hello_world() -> str:
    print('Hello world')


if __name__ == '__main__':
    oops_decorator(say_hello_world)()

    # say_hello_world()
    # print('before!!')
    # say_hello_world1 = oops_decorator(say_hello_world)
    # say_hello_world1()
    # print('hehe')
    # say_hello_world()
