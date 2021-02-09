from django.test import TestCase
from django.utils import timezone


from .models import Pokemon, PokemonType


class PokemonTest(TestCase):
    def create_pokemon(self, id="1000", name="Future Pokemon"):
        return Pokemon.objects.create(id=id, name=name)

    def test_pokemon_creation(self):
        p = self.create_pokemon()
        self.assertTrue(isinstance(p, Pokemon))
        self.assertEqual(str(p), "Future Pokemon")