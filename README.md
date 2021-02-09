# Mapologo-pokeapi

Yet another PokeAPI search app by mapologo.

This is a very simple application to search for pokemon in PokeAPI
https://pokeapi.co

To be able to perform searches with partial names of pokemon you must preload
the database using the command:

```bash
$ python manage.py get_pokemons -f [initial pokemon ID] -t [final pokemon ID] -t [final pokemon ID]
```

This way, it loads the names and identifiers of the pokemons and some additional
information such as the species and type of pokemon.

Once this is done, all you have to do is run the development server and start
searching for Pokemons.

```bash
$ python manage.py runserver
```

There are many things to improve, for example displaying Pokemon information
individually using a modal view. Or perform searches by additional
characteristics such as pokemon type, generation, ranges of values in the
statistics, among others.

To be able to do this it would be necessary to preload more information, and
improve the information display views, but all the basic procedure is already
configured.

Any advice or suggestion is welcome.


