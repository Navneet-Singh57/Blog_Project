# Generated by Django 5.0.6 on 2024-06-19 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_postmodel_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ['-date_created']},
        ),
    ]
