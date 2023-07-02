from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        else:
            return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        try:
            pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
            self.pokemons.remove(pokemon)
            return f'You have released {pokemon_name}'
        except IndexError:
            return 'Pokemon is not caught'

    def trainer_data(self):
        data = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        data += '\n'.join([f'- {p.pokemon_details()}' for p in self.pokemons])
        return data
