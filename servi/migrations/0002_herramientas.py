# Generated by Django 5.1.3 on 2024-12-14 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('caracteristica', models.TextField()),
                ('coste', models.IntegerField()),
                ('fechaVen', models.DateField()),
                ('manual', models.BooleanField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servi.marcaher')),
            ],
        ),
    ]
