class CountVectorizer:
    '''Convert a collection of text to ...'''
    
    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}
		
    def fit_transform(self, corpus):
        pass

    def get_feature_names(self):
        return self._vocabulary.items()

    @property
    def get_feature_names(self):
        return self._vocabulary.items()

if __name__ == '__main__':
    print(CountVectorizer.__doc__)
    print(CountVectorizer.__name__)
    print(CountVectorizer().__class__)

    vec = CountVectorizer()
    print(id(vec))
    print(CountVectorizer.fit_transform)

    # print(vec.get_feature_names)
    # print(vec.get_feature_names.__self__ is vec)
    print(vec.get_feature_names)

