# Generated by Django 3.2.1 on 2021-06-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='fav', to='recipe_app.Author'),
        ),
    ]
