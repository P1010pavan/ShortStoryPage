# Generated by Django 3.0.5 on 2020-04-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20200423_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
