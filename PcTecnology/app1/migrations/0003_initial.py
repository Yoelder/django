# Generated by Django 4.0.6 on 2024-02-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_delete_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.AutoField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('credito', models.CharField(max_length=50)),
            ],
        ),
    ]

