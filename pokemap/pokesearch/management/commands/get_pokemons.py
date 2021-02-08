from django.core.management.base import BaseCommand, CommandError
from pokesearch.models import Pokemon, PokemonSpecies, Type, PokemonType

import requests
import requests_cache


requests_cache.install_cache('pokesearch_cache')


class Command(BaseCommand):
    help = "Get the list of Pokemons from PokeAPI"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--from", type=int, default=1)
        parser.add_argument("-t", "--to", type=int, default=899)

    def handle(self, *args, **options):
        _from = options["from"]
        _to = options["to"]
        for pokemon_id in range(_from, _to):
            pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
            pokemon_obj, pokemon_created = Pokemon.objects.get_or_create(
                id=pokemon.json()["id"], name=pokemon.json()["name"]
            )
            species = requests.get(pokemon.json()["species"]['url'])
            species_obj, species_created = PokemonSpecies.objects.get_or_create(
                id=species.json()["id"], name=species.json()["name"]
            )
            pokemon_obj.species = species_obj
            for pokemon_type in pokemon.json()["types"]:
                type_ = requests.get(pokemon_type["type"]["url"])
                type_obj, type_created = Type.objects.get_or_create(
                    id=type_.json()["id"], name=type_.json()["name"]
                )
                (
                    pokemon_type_obj,
                    pokemon_type_created,
                ) = PokemonType.objects.get_or_create(
                    slot=pokemon_type["slot"], pokemon=pokemon_obj, type=type_obj
                )
            pokemon_obj.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully added pokemon [{pokemon.json()['id']}]: {pokemon.json()['name']}"
                )
            )
