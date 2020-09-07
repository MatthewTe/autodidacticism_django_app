# Generated by Django 3.1 on 2020-09-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_resources', '0007_auto_20200904_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources_index_card',
            name='button_a_href',
        ),
        migrations.RemoveField(
            model_name='resources_index_card',
            name='button_b_href',
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.CharField(help_text='A seralized list of categories that the article belongs to.', max_length=255, null=True, verbose_name='MetaData Article Categories'),
        ),
        migrations.AlterField(
            model_name='resources_index_card',
            name='button_a_icon',
            field=models.CharField(default='posts_icon.png', help_text='The name of the icon image to be inserted into the first button.', max_length=50, verbose_name='Button A Icon'),
        ),
        migrations.AlterField(
            model_name='resources_index_card',
            name='button_b_icon',
            field=models.CharField(default='catalogue_icon.png', help_text='The name of the icon image to be inserted into the second button.', max_length=50, verbose_name='Button B Icon'),
        ),
    ]
