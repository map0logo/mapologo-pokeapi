from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

import requests
import requests_cache

from .models import Pokemon


requests_cache.install_cache('pokesearch_cache')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Pokemon
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Pokemon.objects.filter(
            Q(name__icontains=query)
        )

        for obj in object_list:
            pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{obj.id}")
            obj.sprite_url = pokemon.json()["sprites"]["front_default"]
            obj.height = pokemon.json()["height"]
            obj.weight = pokemon.json()["weight"]
        return object_list