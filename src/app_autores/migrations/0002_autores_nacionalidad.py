# Generated by Django 5.2 on 2025-04-08 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_autores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autores',
            name='nacionalidad',
            field=models.CharField(choices=[('AR', 'Argentina'), ('BO', 'Boliviana'), ('BR', 'Brasileña'), ('CL', 'Chilena'), ('CO', 'Colombiana'), ('CR', 'Costarricense'), ('CU', 'Cubana'), ('DO', 'Dominicana'), ('EC', 'Ecuatoriana'), ('SV', 'Salvadoreña'), ('GT', 'Guatemalteca'), ('HN', 'Hondureña'), ('MX', 'Mexicana'), ('NI', 'Nicaragüense'), ('PA', 'Panameña'), ('PY', 'Paraguaya'), ('PE', 'Peruana'), ('PR', 'Puertorriqueña'), ('UY', 'Uruguaya'), ('VE', 'Venezolana'), ('ES', 'Española'), ('US', 'Estadounidense'), ('CA', 'Canadiense'), ('FR', 'Francesa'), ('DE', 'Alemana'), ('IT', 'Italiana'), ('PT', 'Portuguesa'), ('GB', 'Británica'), ('IE', 'Irlandesa'), ('CN', 'China'), ('JP', 'Japonesa'), ('KR', 'Coreana'), ('IN', 'India'), ('RU', 'Rusa'), ('AU', 'Australiana'), ('ZA', 'Sudafricana'), ('EG', 'Egipcia'), ('NG', 'Nigeriana'), ('KE', 'Keniata'), ('MA', 'Marroquí')], default='AR', max_length=10),
        ),
    ]
