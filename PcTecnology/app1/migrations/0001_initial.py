# Generated by Django 4.0.6 on 2024-01-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=100)),
                ('ganancias', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
