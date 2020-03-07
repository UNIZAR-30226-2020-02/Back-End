# Generated by Django 2.2.11 on 2020-03-07 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('IDAudio', models.IntegerField(primary_key=True, serialize=False)),
                ('FicheroDeAudio', models.FileField(upload_to='')),
                ('Titulo', models.CharField(max_length=30)),
                ('Idioma', models.CharField(max_length=15)),
                ('Duracion', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PlayStack.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='CreadorContenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PlayStack.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='NoPremium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PlayStack.Usuario')),
                ('NumSalt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PlayStack.Audio')),
                ('Resumen', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePremium', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PlayStack.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Nombre', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Contrasenya', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=100)),
                ('FotoDePerfil', models.ImageField(upload_to='')),
                ('Seguidos', models.ManyToManyField(related_name='_usuario_Seguidos_+', to='PlayStack.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('IDPlayList', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('UsuarioNombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayStack.Usuario')),
            ],
            options={
                'unique_together': {('IDPlayList', 'UsuarioNombre')},
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=1000)),
                ('Canciones', models.ManyToManyField(to='PlayStack.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='Carpeta',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('PlayList', models.ManyToManyField(to='PlayStack.PlayList')),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='CreadorDeContenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayStack.CreadorContenido'),
        ),
        migrations.AddField(
            model_name='audio',
            name='UsuariosComoFavorita',
            field=models.ManyToManyField(to='PlayStack.Usuario'),
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('Nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('PaisDeNacimiento', models.CharField(max_length=15)),
                ('Canciones', models.ManyToManyField(to='PlayStack.Audio')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='audio',
            unique_together={('IDAudio', 'CreadorDeContenido')},
        ),
    ]
