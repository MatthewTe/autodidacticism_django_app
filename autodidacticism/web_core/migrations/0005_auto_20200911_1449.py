# Generated by Django 3.1.1 on 2020-09-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_core', '0004_auto_20200911_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications_index_cards',
            name='card_category',
            field=models.CharField(choices=[('web_applications', 'web_applications'), ('finance_applications', 'finance_applications'), ('abm_applications', 'abm_applications'), ('data_pipeline_applications', 'data_pipeline_applications')], help_text='The category of project that the card relates to. It is used by the templating engine to sort the card.', max_length=50, verbose_name='Card Application Category'),
        ),
    ]
