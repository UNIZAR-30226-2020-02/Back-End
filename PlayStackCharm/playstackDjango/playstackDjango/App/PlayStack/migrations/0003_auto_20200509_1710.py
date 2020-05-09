# Generated by Django 2.1.7 on 2020-05-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayStack', '0002_podcast_fotodelpodcast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='Capitulos',
        ),
        migrations.AddField(
            model_name='podcast',
            name='Capitulos',
            field=models.ManyToManyField(related_name='Capitulos', to='PlayStack.Capitulo'),
        ),
    ]
