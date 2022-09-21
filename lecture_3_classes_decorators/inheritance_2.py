class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


class CountVectorizer(BaseEstimator):
    def to_str(self):
        base_str = BaseEstimator.to_str(self)  # НО! есть способ лучше
        return f'[{base_str}]'


if __name__ == '__main__':
    print(CountVectorizer().to_str())
