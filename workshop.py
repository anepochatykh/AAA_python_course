class BaseClass:
	def __init__(self, base_param=None):
		self.base_param = base_param
	

class CountVectorizer(BaseClass):
    def __init__(self, lowercase=True):
        super().__init__(base_param=lowercase)
        self.lowercase = lowercase


class Person:
    def __init__(self):
        self.first_name = 'John'
        self.last_name = 'Doe'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


import sys

tuple_pokemon = ('Pikachu', 'Mouse', 5.99, 40.64, ['Electric'], ['Ground'])

# Dict
dict_pokemon = {
	'name': 'Pikachu', 'category': 'Mouse', 'height': 40.64,
	'weight': 5.99, 'strengths': ['Electric'], 'weaknesses': ['Ground'],
}


if __name__ == '__main__':
    print(sys.getsizeof(tuple_pokemon))
    print(sys.getsizeof(dict_pokemon))
    print(tuple_pokemon[4])
