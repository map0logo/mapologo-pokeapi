from django.db import models
from django.utils.translation import gettext_lazy as _


class PokemonSpecies(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="The identifier for this resource."
    )
    name = models.CharField(
        _("name"), max_length=32, help_text="The name for this resource."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pokemon species"
        verbose_name_plural = "Pokemon species"
        ordering = ['id']


class Type(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="The identifier for this resource."
    )
    name = models.CharField(
        _("name"), max_length=32, help_text="The name for this resource."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
        ordering = ['id']


class Pokemon(models.Model):
    id = models.IntegerField(
        primary_key=True, help_text="The identifier for this resource."
    )
    name = models.CharField(
        _("name"), max_length=32, help_text="The name for this resource."
    )
    species = models.ForeignKey(
        PokemonSpecies,
        on_delete=models.CASCADE,
        help_text="The species this Pokémon belongs to.",
        blank=True,
        null=True,
    )
    types = models.ManyToManyField(
        Type,
        through="PokemonType",
        help_text="A list of details showing types this Pokémon has.",
        blank=True
    )
    created = models.DateTimeField(
        _("Creation Date and Time"),
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        _("Modification Date and Time"),
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
        ordering = ['id']


class PokemonType(models.Model):
    slot = models.IntegerField(
        _("slot"), help_text="The order the Pokémon's types are listed in."
    )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pokemon.name}: {self.slot}: {self.type.name}"

    class Meta:
        verbose_name = "Pokemon type"
        verbose_name_plural = "Pokemon types"
        ordering = ['pokemon', 'slot']
