# Generated by Django 3.1.6 on 2021-02-04 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokesearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemon',
            options={'verbose_name': 'Pokemon', 'verbose_name_plural': 'Pokemons'},
        ),
        migrations.AlterModelOptions(
            name='pokemonspecies',
            options={'verbose_name': 'Pokemon species', 'verbose_name_plural': 'Pokemon species'},
        ),
        migrations.AlterModelOptions(
            name='pokemontype',
            options={'verbose_name': 'Pokemon type', 'verbose_name_plural': 'Pokemon types'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='species',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='species',
            field=models.ForeignKey(default=None, help_text='The species this Pokémon belongs to.', on_delete=django.db.models.deletion.CASCADE, to='pokesearch.pokemonspecies'),
        ),
    ]
