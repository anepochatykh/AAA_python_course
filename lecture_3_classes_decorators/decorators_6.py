from typing import Callable


# проброс аргументов декоратору
def enclose_with_tags(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '<Entity>{}</Entity>'.format(result)
    return wrapper


@enclose_with_tags
def say_hi(name: str) -> str:
    return 'Hi, {}'.format(name)


if __name__ == '__main__':
    print(say_hi('Bob'))
