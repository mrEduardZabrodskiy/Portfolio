# Generated by Django 5.0.7 on 2024-07-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0009_alter_softskill_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='in_tech',
            field=models.BooleanField(default=True),
        ),
    ]
