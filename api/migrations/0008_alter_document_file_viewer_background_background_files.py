# Generated by Django 4.1.5 on 2023-01-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_document_document_file_viewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document_file_viewer_background',
            name='background_files',
            field=models.FileField(upload_to='documents/background_files/'),
        ),
    ]