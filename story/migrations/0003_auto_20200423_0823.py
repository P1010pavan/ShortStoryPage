# Generated by Django 3.0.5 on 2020-04-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='Date',
            field=models.DateField(),
        ),
    ]