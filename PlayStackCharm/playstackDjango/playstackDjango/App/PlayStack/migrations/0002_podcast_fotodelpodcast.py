# Generated by Django 2.1.7 on 2020-05-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayStack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='FotoDelPodcast',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
