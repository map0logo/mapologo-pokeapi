# Generated by Django 3.1.6 on 2021-02-04 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokesearch', '0002_auto_20210204_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='species',
            field=models.ForeignKey(blank=True, help_text='The species this Pokémon belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='pokesearch.pokemonspecies'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(blank=True, help_text='A list of details showing types this Pokémon has.', null=True, through='pokesearch.PokemonType', to='pokesearch.Type'),
        ),
    ]
