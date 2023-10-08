class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(C, B):
    pass


if __name__ == '__main__':
    pass
    # for idx, cur_level in enumerate(D.mro()):
    #     print(idx, cur_level)
