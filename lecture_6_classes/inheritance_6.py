class A:
    def process(self):
        print('A.process')


class B(A):
    def process(self):
        print('B.process')
        super().process()


class C(B):
    def process(self):
        print('C.process')
        super().process()


class D(C):
    pass


class E:
    pass


if __name__ == '__main__':
    print(issubclass(A, (C, B)))
