# Generated by Django 4.1.5 on 2023-01-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_document_file_viewer_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file_viewer',
            field=models.ManyToManyField(related_name='Document_background', to='api.document_file_viewer_background'),
        ),
    ]