# Generated by Django 4.2.7 on 2023-11-30 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_apigenres_apigenresmovies_apimoviecastingcredits_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="genres",
            table="genres",
        ),
        migrations.AlterModelTable(
            name="moviecastingcredits",
            table="movie_casting_credits",
        ),
        migrations.AlterModelTable(
            name="movies",
            table="movies",
        ),
        migrations.AlterModelTable(
            name="people",
            table="people",
        ),
        migrations.AlterModelTable(
            name="peoplealiases",
            table="people_aliases",
        ),
    ]
