class CountVectorizer:
    stop_words = ('a', 'b', 'c')

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def get_stop_words(self):
        return self.stop_words + ('d', 'e', 'f')

if __name__ == '__main__':
    c = CountVectorizer()
    d = CountVectorizer()

    print(CountVectorizer.get_stop_words)
    print()
    print(c.get_stop_words)
    print()
    print(d.get_stop_words)
    print(c.get_stop_words == d.get_stop_words)
    print(c.__class__.get_stop_words == d.__class__.get_stop_words)
