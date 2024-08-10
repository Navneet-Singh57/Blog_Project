# Generated by Django 5.0.6 on 2024-06-19 16:53

import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profilemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.png', upload_to=users.utils.user_profile_path),
        ),
    ]
