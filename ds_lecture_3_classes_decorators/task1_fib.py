from functools import lru_cache


@lru_cache()
def calc_fibonachi(n):
    if n == 0 or n == 1:
        return n
    return calc_fibonachi(n - 1) + calc_fibonachi(n - 2)


if __name__ == '__main__':
    print(calc_fibonachi(100))
