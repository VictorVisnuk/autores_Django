# Generated by Django 5.2 on 2025-04-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_fallecimiento', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
