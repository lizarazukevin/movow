# Generated by Django 4.2.7 on 2023-12-06 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_genres_table_alter_moviecastingcredits_table_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ApiGenres",
        ),
        migrations.DeleteModel(
            name="ApiGenresMovies",
        ),
        migrations.DeleteModel(
            name="ApiMoviecastingcredits",
        ),
        migrations.DeleteModel(
            name="ApiMovies",
        ),
        migrations.DeleteModel(
            name="ApiPeople",
        ),
        migrations.DeleteModel(
            name="ApiPeoplealiases",
        ),
    ]
