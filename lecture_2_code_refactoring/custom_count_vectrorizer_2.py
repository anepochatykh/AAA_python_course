class CountVectorizer():
	""" Convert a collection of text """ 	# docstring класса
	stop_words = ('a', 'the', 'and') 		# атрибут класса

	def __init__(self, lowercase=True): 	# аналог конструктора
		self.lowercase = lowercase			# атрибут объекта (экземпляра) класса
		self._vocabulary = {}
		self.__vocabulary = {}

	def get_feature_names(self):
		return self._vocabulary.items()

	@staticmethod
	def split(text: str) -> [str]:
		return text.split()

	@classmethod
	def from_vocabulary(cls, vocabulary):
		print(cls, type(cls))
		vec = cls()
		vec._vocabulary = vocabulary
		return vec

	@property
	def feature_names(self):
		return self._vocabulary.items()


if __name__ == '__main__':
	# print(CountVectorizer.get_feature_names)
	# # Out:<function __main__.CountVectorizer.get_feature_names(self)>
	#
	# vec = CountVectorizer()
	# print('vec.get_feature_names', vec.get_feature_names)
	# # <bound method CountVectorizer.get_feature_names of CountVectorizer()>
	#
	# print('vec.get_feature_names.__self__ is vec', vec.get_feature_names.__self__ is vec)
	# # True
	#
	# print('CountVectorizer.split', CountVectorizer.split('Crock Pot Pasta'))
	# # Out: ['Crock', 'Pot', 'Pasta']
	#
	# vec = CountVectorizer()
	# print('vec.split', vec.split('Crock Pot Pasta'))
	# # Out: ['Crock', 'Pot', 'Pasta']
	#
	# vec = CountVectorizer.from_vocabulary({"Crock": 0, "Pot": 1, "Pasta": 2})
	# print('vec._vocabulary', vec._vocabulary)
	# # Out: {‘Crock’: 0, ‘Pot’: 1, ‘’Pasta’: 2}
	#
	# vec2 = vec.from_vocabulary({"Crock": 0, "Pot": 1, "Pasta": 2})

	vec = CountVectorizer()
	print('vec.feature_names', vec.feature_names)
	# Out: dict_items([])







