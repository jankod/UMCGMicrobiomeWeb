# Generated by Django 2.1.3 on 2018-11-24 22:32

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181124_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='public',
            new_name='is_public',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=40000),
        ),
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[(app.models.ProjectStatus('Active'), 'Active'), (app.models.ProjectStatus('Not active'), 'Not active')], max_length=20),
        ),
    ]
