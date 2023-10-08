class BaseEstimator:
    def to_str(self):
        return f'{self.__class__.__name__}'


class BaseVectorizer():
    def get_stop_words(self):
        return self._stop_words


class CountVectorizer(BaseVectorizer, BaseEstimator):
    def __init__(self):
        self._stop_words = ('and', 'or', 'the')


if __name__ == '__main__':
    vec = CountVectorizer()
    print(vec.get_stop_words())
    # Out: ('and', 'or', 'the')

    print(vec.to_str())
    # Out: 'CountVectorizer'
