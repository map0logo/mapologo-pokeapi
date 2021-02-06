from django.contrib import admin
from .models import Pokemon, PokemonSpecies, Type, PokemonType

class PokemonTypeInline(admin.TabularInline):
    model = PokemonType
    extra = 0

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    inlines = (PokemonTypeInline,)
    list_display = ('id', 'name')
    search_fields = ('name', )

@admin.register(PokemonSpecies)
class PokemonSpeciesAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('id', 'name')

@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    search_fields = ('pokemon__name', 'type__name')
    list_display = ('pokemon', 'slot', 'type')

