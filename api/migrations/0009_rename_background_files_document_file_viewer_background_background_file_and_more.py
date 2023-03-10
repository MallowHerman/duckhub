# Generated by Django 4.1.5 on 2023-01-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_document_file_viewer_background_background_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document_file_viewer_background',
            old_name='background_files',
            new_name='background_file',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file_viewer',
            field=models.ManyToManyField(related_name='document_background_files', to='api.document_file_viewer_background'),
        ),
    ]
