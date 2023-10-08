# Напишите миксин EmojiMixin, который модифицирует метод __str__
# Заменяет категорию покемона на эмоджи

# grass => 🌿
# fire => 🔥
# water => 🌊
# electric => ⚡

# со звездочкой
# EmojiMixin внутри знает только category


class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    EMOJI_DICT = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡'}

    def __str__(self):
        # return f'{self.name}/{EmojiMixin.EMOJI_DICT[self.category]}'
        s = super().__str__()
        return s.replace(self.category, EmojiMixin.EMOJI_DICT[self.category])


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name, category, weaknesses=None):
        super().__init__(name, category)
        self._weaknesses = weaknesses

    @property
    def weaknesses(self):
        if self._weaknesses:
            return self._weaknesses[0]
        return None


if __name__ == '__main__':
    bulbasaur = Pokemon(
        name='Bulbasaur',
        category='seed',
        weaknesses=('fire', 'psychic', 'flying', 'ice')
    )
    print(bulbasaur.weaknesses)

    base_charmander = BasePokemon(name='Charmander', category='Lizard')
    print(base_charmander)

    pikachu = Pokemon(name='Pikachu', category='electric')
    print(pikachu)
