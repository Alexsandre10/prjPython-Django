# Generated by Django 2.0.5 on 2018-05-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/imagens', verbose_name='Imagem'),
        ),
    ]
