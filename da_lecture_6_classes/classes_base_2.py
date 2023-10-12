# Покемон
# - Имя: Pikachu
# - Категория: Mouse
# - Рост: 40.64 см
# - Вес: 5.99 кг
# - Сильные стороны: Electric
# - Слабые стороны: Ground


# добавим некоторые действия к покемону


# Tuple
tuple_pokemon = ('Pikachu', 'Mouse', 5.99, 40.64, ['Electric'], ['Ground'])

def grow(pokemon, extra_height: float):
	name, category, weight, height, strengths, weaknesses = pokemon
	return (name, category, weight, height + extra_height, strengths, weaknesses)

def add_strength(pokemon, strength: str):
	name, category, weight, height, strengths, weaknesses = pokemon
	return (name, category, weight, height, strengths + [strength], weaknesses)


# Dict
dict_pokemon = {
	'name': 'Pikachu', 'category': 'Mouse', 'height': 40.64,
	'weight': 5.99, 'strengths': ['Electric'], 'weaknesses': ['Ground'],
}

def grow(pokemon, extra_height: float):
	pokemon['height'] += extra_height
	return pokemon

def add_strength(pokemon, strength: str):
	pokemon['strengths'].append(strength)
	return pokemon


# Namedtuple
from collections import namedtuple
attributes = ['name', 'category', 'height', 'weight', 'strengths', 'weaknesses']
Pokemon = namedtuple('Pokemon', attributes)
pikachu = Pokemon(name='Pikachu', category='Mouse', height=40.64, 
		  weight=5.99,strengths=['Electric'], weaknesses=['Ground'],)


def grow(pokemon, extra_height: float):
	return pokemon._replace(height=pokemon.height + extra_height)

def add_strength(pokemon, strength: str):
	return pokemon._replace(strengths=pokemon.strengths + [strength])


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

	def grow(self, extra_height):
		self.height += extra_height

	def add_strength(self, strength: str):
		self.strengths.append(strength)

