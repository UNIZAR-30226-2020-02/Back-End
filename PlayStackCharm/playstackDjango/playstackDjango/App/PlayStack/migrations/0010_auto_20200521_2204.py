# Generated by Django 3.0.6 on 2020-05-21 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlayStack', '0009_auto_20200521_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='podcast',
            name='Tematica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tematica', to='PlayStack.Tematica'),
        ),
    ]
