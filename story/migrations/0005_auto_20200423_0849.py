# Generated by Django 3.0.5 on 2020-04-23 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20200423_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]