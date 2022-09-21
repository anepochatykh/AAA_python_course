class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


class CountVectorizer(BaseEstimator):
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}


if __name__ == '__main__':
    print(CountVectorizer().to_str())
