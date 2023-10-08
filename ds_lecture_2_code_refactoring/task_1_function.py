# If the number can be divided by 3, it will output Fizz instead of the number.
# If the number is divisible by 5, the result will display Buzz instead of the number.
# And if the given number is divisible by both 3 and 5, Fizz Buzz will be printed instead o
# Fuzz buzz тест - тест, которые выводит Fuzz, если число делится на 3, Buzz, если число делится на 5, FuzzBuzz, если число делится и на 3 и на 5, и само число в остальных случаях
# Задание
# Написать функцию custom_fuzz_buzz, которая делает fuzz_buzz тест, с такими параметрами
#     slice - какой-то контейнер (Iterable)
#     start/end - начало и конец для range
# Указывать либо slice, либо start/end, в остальных случая выбрасывать исключение


def fuzz_buzz(slice):
    for el in slice:
        if el % 3 == 0 and el % 5 == 0:
            print('FuzzBuzz')
        elif el % 3 == 0:
            print('Fuzz')
        elif el % 5 == 0:
            print('Buzz')
        else:
            print(el)


def custom_fuzz_buzz(slice=None, start=None, end=None):
    if slice:
        fuzz_buzz(slice)
    elif start and end:
        fuzz_buzz(range(start, end))


if __name__ == "__main__":
    print('===')
    custom_fuzz_buzz(slice=[1,2,3,4,5,6])
    print('===')
    custom_fuzz_buzz(start=1, end=10)
    # f = get_func(True)
    # f()


# или функцию, которая будет принимать на вход что-то другое....
# или
