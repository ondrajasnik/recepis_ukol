# Generated by Django 3.0.2 on 2020-01-30 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0010_auto_20200130_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredients',
            name='unit',
        ),
    ]
