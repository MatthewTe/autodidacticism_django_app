# Generated by Django 3.1 on 2020-09-01 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education_resources', '0002_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='posted_on',
            new_name='created_date',
        ),
    ]