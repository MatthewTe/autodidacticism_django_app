# Generated by Django 3.1.1 on 2020-09-17 04:35

from django.db import migrations, models
import django.db.models.deletion
import education_resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('education_resources', '0009_auto_20200911_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the catalogue element. Will be displayed as the title of the element index card.', max_length=100, verbose_name='Element Title')),
                ('card_image', models.CharField(help_text='The name of the image file that is contained in a static directory that will be used as an index card thumbnail', max_length=100, verbose_name='Card Image Thumbnail')),
                ('description', models.TextField(help_text='The Description of the catalogue element. The field will be displayed as the main text block in an element index card.', verbose_name='Element Description')),
                ('source', models.CharField(help_text='Either an author name, or a direct formal citation for the content represented by the model instance.', max_length=255, verbose_name='Source')),
                ('file', models.FileField(help_text='This is the pdf file connected to an element index card. This is the pdf that is displayed by an imbeded js renderer.', upload_to=education_resources.models.CatalogueElement.build_pdf_file_path, verbose_name='PDF File')),
                ('category', models.ForeignKey(help_text='This is a Foregin Key that connects to a Resource Index Card Instance that is used to sort into a category.', on_delete=django.db.models.deletion.CASCADE, to='education_resources.resources_index_card', verbose_name='Element Category')),
            ],
        ),
    ]