# Покемон
# - Имя: Pikachu
# - Категория: Mouse
# - Рост: 40.64 см
# - Вес: 5.99 кг
# - Сильные стороны: Electric
# - Слабые стороны: Ground


# добавим Iron Man 

# iron man
# - Iron Man
# - Рост: 180 см
# - Вес: 300 кг
# - скорость: 200 км/ч


# Tuple
tuple_pokemon = ('Pikachu', 'Mouse', 5.99, 40.64, ['Electric'], ['Ground'])
# add Iron Man
tuple_iron_man = ('Iron Man', 180, 300, 200)


def grow(pokemon, extra_height: float):
	name, category, weight, height, strengths, weaknesses = pokemon
	return (name, category, weight, height + extra_height, strengths, weaknesses)

def speed_up(iron_man, extra_speed: float):
	name, weight, height, speed = iron_man
	return (name, weight, height, speed + extra_speed)


# Dict
dict_pokemon = {
	'name': 'Pikachu', 'category': 'Mouse', 'height': 40.64,
	'weight': 5.99, 'strengths': ['Electric'], 'weaknesses': ['Ground'],
}
dict_iron_man = {
	'name': 'Iron Man', 'height': 180, 'weight': 300, 'speed': 200,
}

def grow(pokemon, extra_height: float):
	pokemon['height'] += extra_height
	return pokemon

def speed_up(iron_man, extra_speed: float):
	iron_man['speed'] += extra_speed
	return iron_man


# Namedtuple
from collections import namedtuple
attributes = ['name', 'category', 'height', 'weight', 'strengths', 'weaknesses']
Pokemon = namedtuple('Pokemon', attributes)
pikachu = Pokemon(name='Pikachu', category='Mouse', height=40.64, 
		  weight=5.99,strengths=['Electric'], weaknesses=['Ground'],)

IronMan = namedtuple('IronMan', ['name', 'height', 'weight', 'speed'])
iron_man = IronMan(name='Iron Man', height=180, weight=300, speed=200)

def grow(pokemon, extra_height: float):
	return pokemon._replace(height=pokemon.height + extra_height)

def speed_up(iron_man, extra_speed: float):
	return iron_man._replace(height=iron_man.speed + extra_speed)


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
pokemon = Pokemon(
	name='Pikachu', category='Mouse', height=40.64, 
	weight=5.99,strengths=['Electric'], weaknesses=['Ground'],
)
pokemon.grow(10)


class IronMan:
	def __init__(self, name: str, height: float, weight: float, speed: float):
		self.name = name
		self.height = height
		self.weight = weight
		self.speed = speed

	def speed_up(self, extra_speed):
		self.speed += extra_speed
	
iron_man = IronMan(name='Iron Man', height=180, weight=300, speed=200)
iron_man.speed_up(100)
