# Generated by Django 5.0.2 on 2024-02-29 20:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_filemodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]