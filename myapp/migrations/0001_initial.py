# Generated by Django 4.1.7 on 2023-04-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('inputAddress', models.CharField(max_length=40)),
                ('inputCity', models.CharField(max_length=40)),
                ('inputState', models.CharField(max_length=40)),
                ('inputZip', models.CharField(max_length=40)),
                ('inputRecuperacion', models.CharField(max_length=40)),
            ],
        ),
    ]
