# Generated by Django 3.0.5 on 2020-04-23 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20200423_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='Description_Story',
            new_name='Story_Description',
        ),
        migrations.RenameField(
            model_name='upload',
            old_name='Name_of_the_story',
            new_name='Title_of_the_story',
        ),
        migrations.RenameField(
            model_name='upload',
            old_name='Name',
            new_name='Your_Name',
        ),
    ]
