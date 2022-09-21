from typing import Iterable


def print_iterable(iterable: Iterable):
    it = iter(iterable)  # получаем итератор
    while True:
        try:
            # next(it) возвращает следующий элемент из итератора
            print(next(it), end=' ')
        except StopIteration:  # если при вызове next(it) нет следующего элемента, то
            break


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print_iterable(l)

    d = {1: 1, 2: 2, 3: 3}
    print_iterable(d)
