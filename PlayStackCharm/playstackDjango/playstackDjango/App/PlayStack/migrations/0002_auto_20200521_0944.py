# Generated by Django 3.0.6 on 2020-05-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayStack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='Capitulos',
            field=models.ManyToManyField(blank=True, related_name='Capitulos', to='PlayStack.Capitulo'),
        ),
    ]
