# 1
# Дана функция обучения покемона train
# Измените класс Pokemon так, чтобы обучение проходило без ошибок

# 2
# Напишите класс Digimon так, чтобы обучение проходило без ошибок

# 3
# Напишите абстрактный класс AnimeMon:
#   Имеет абстрактный метод inc_exp
#   Имеет абстрактное свойство exp
#   Классы Digimon и Pokemon наследуются от AnimeMon

from abc import ABC, abstractmethod


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_experience(self, value):
        ...

    @property
    @abstractmethod
    def experience(self):
        ...


class BasePokemon(PokemonTrainInterface):
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._experience = 100

    def __str__(self):
        return f'{self.name}/{self.category}'

    def increase_experience(self, value: int):
        self._experience += value

    @property
    def experience(self):
        return self._experience


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses=None):
        super().__init__(name, category)
        self._weaknesses = weaknesses

    @property
    def weaknesses(self):
        if self._weaknesses:
            return self._weaknesses[0]
        return None


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', category='grass')
    bulbasaur.increase_experience(100)
    # print(bulbasaur.experience())
    assert bulbasaur.experience == 200, 'Try harder, Neeman'
