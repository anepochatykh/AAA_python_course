def custom_sum(*args) -> int:
    result = 0
    print(args, type(args))
    for n in args:
        result += n
    return result


if __name__ == '__main__':
    print(custom_sum())

    print(custom_sum(1, 3, 10, 1000))

    print(custom_sum(1, 3, 10, -1000))

    args = [1, 3, 10, -1000]
    print(custom_sum(*args))
