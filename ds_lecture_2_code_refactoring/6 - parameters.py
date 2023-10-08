def say_hello(name: str, border: str = '-') -> str:
    """Wraps the `name` with the specified `border`."""
    return f'{border} Hello, {name}{border}'


if __name__ == '__main__':
    print(say_hello('my friend'))
    # - Hello, my friend-

    print(say_hello('my friend', '=='))
    # == Hello, my friend==

    print(say_hello('==', 'my friend'))

    print(say_hello(border='*', name='my friend'))
    # * Hello, my friend*
