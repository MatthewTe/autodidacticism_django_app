# Generated by Django 3.1 on 2020-09-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_resources', '0005_auto_20200904_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_category',
            field=models.CharField(help_text='The associated Article Index Card model Instance.', max_length=200, verbose_name='Main Article Category'),
        ),
    ]
