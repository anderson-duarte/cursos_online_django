# Generated by Django 3.0.5 on 2020-04-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20200414_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/', verbose_name='Inserir Imagem'),
        ),
    ]