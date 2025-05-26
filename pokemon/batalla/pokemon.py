import move
import stat
import requests


class Pokemon:
    def __init__(self, id, name=None):
        def pokemonById(id):
            URL = f"https://pokeapi.co/api/v2/pokemon/{id}/"
            # Making a get request
            response = requests.get(URL)

            # print response
            # print(response)

            # print json content
            return response.json()

        response = pokemonById(id)
        # self.moves
        self.species_name = response["species"]["name"]
        # self.stats
        self.name = name if name is not None else response["name"]

        print(f"Hola soy {self.name} y soy un {self.species_name}")

    def atacar(self):
        pass

    def encajar(self):
        pass


if __name__ == "__main__":
    pokejemplo = Pokemon(4, "Manolo")
