class CountVectorizer():
	""" Convert a collection of text """ 	# docstring класса
	stop_words = ('a', 'the', 'and') 		# атрибут класса

	def __init__(self, lowercase=True): 	# аналог конструктора
		self.lowercase = lowercase			# атрибут объекта (экземпляра) класса
		self._vocabulary = {}
		self.__vocabulary = {}

	def fit_transform(self, corpus):		# метод
		""" Learn the vocabulary """ 		# docstring метода
		pass

	def get_id(self):
		return id(self)


if __name__ == '__main__':
	# vec == self
	vec = CountVectorizer()
	print(vec.get_id() == id(vec))

	# stop_words id
	v1, v2 = CountVectorizer(), CountVectorizer()
	print('attr class', id(v1.stop_words) == id(v2.stop_words))

	# private attributes
	print(f'vec._vocabulary : {vec._vocabulary}')
	print(f'vec._CountVectorizer__vocabulary : {vec._CountVectorizer__vocabulary}')
	print(f'vec.__vocabulary : {vec.__vocabulary}')



