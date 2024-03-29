# опишем Покемона
# Покемон
# - Имя: Pikachu
# - Категория: Mouse
# - Рост: 40.64 см
# - Вес: 5.99 кг
# - Сильные стороны: Electric
# - Слабые стороны: Ground

# Какие варианты ? 

# Tuple
tuple_pokemon = ('Pikachu', 'Mouse', 5.99, 40.64, ['Electric'], ['Ground'])

# Dict
dict_pokemon = {
	'name': 'Pikachu', 'category': 'Mouse', 'height': 40.64,
	'weight': 5.99, 'strengths': ['Electric'], 'weaknesses': ['Ground'],
}

# Namedtuple
from collections import namedtuple
attributes = ['name', 'category', 'height', 'weight', 'strengths', 'weaknesses']
Pokemon = namedtuple('Pokemon', attributes)
pikachu = Pokemon(name='Pikachu', category='Mouse', height=40.64, 
		  weight=5.99,strengths=['Electric'], weaknesses=['Ground'],)


# class Pokemon
from typing import List

class Pokemon:
	def __init__(self, name: str, category: str, height: float, weight: float, strengths: List[str], weaknesses: List[str], next_generation=None): 
		self.name = name
		self.category = category
		self.height = height
		self.weight = weight
		self.strengths = strengths
		self.weaknesses = weaknesses
		self.next_generation = next_generation

	def evolve(self):
		if self.next_generation:
			pass
