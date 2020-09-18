# Generated by Django 3.1.1 on 2020-09-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education_resources', '0008_auto_20200905_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, help_text='The date when the article was posted.', verbose_name='Date Posted'),
        ),
    ]