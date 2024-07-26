# Generated by Django 5.0.7 on 2024-07-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0008_remove_softskill_skill_level_softskill_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softskill',
            name='level',
            field=models.CharField(blank=True, choices=[('A1', 'Elementary'), ('A2', 'Pre-intermediate'), ('B1', 'Intermediate'), ('B2', 'Upper intermediate'), ('C1', 'Advanced'), ('C2', 'Proficiency'), ('NA', 'Native')], default='A1', max_length=2),
        ),
    ]