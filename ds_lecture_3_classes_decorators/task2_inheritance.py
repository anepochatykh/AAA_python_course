# Реализуйте класс BasePokemon
# устанавливает атрибуты name и category
# имеет метод __str__, выводящий строку из атрибутов name и category
#
# base_charmander = BasePokemon(name='Charmander', category='Lizard')
# base_charmander.to_str()
# Out: 'Charmander/Lizard'

# charmander = Pokemon(
# name='Charmander',
# category='Lizard',
# weaknesses=(water, ground, rock)
# )
# property weakness -> first weaknesses


class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self._weaknesses = weaknesses

    @property
    def weakness(self):
        return self._weaknesses[0]


if __name__ == '__main__':
    base_charmander = BasePokemon(name='Charmander', category='Lizard')
    print(base_charmander)
    bulbasaur = Pokemon(
        name='Bulbasaur',
        category='seed',
        weaknesses=('fire', 'psychic', 'flying', 'ice')
    )
    print(bulbasaur.weakness)





