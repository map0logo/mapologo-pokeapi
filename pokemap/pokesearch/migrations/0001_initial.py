# Generated by Django 3.1.6 on 2021-02-04 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(help_text='The identifier for this resource.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name for this resource.', max_length=32, verbose_name='name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonSpecies',
            fields=[
                ('id', models.IntegerField(help_text='The identifier for this resource.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name for this resource.', max_length=32, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.IntegerField(help_text='The identifier for this resource.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name for this resource.', max_length=32, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField(help_text="The order the Pokémon's types are listed in.", verbose_name='slot')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokesearch.pokemon')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokesearch.type')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='species',
            field=models.ManyToManyField(help_text='The species this Pokémon belongs to.', to='pokesearch.PokemonSpecies'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(help_text='A list of details showing types this Pokémon has.', through='pokesearch.PokemonType', to='pokesearch.Type'),
        ),
    ]
