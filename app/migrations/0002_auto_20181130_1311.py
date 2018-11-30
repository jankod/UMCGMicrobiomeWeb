# Generated by Django 2.1.3 on 2018-11-30 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_birth', models.SmallIntegerField()),
                ('is_male', models.BooleanField()),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SampleFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField(max_length=240)),
                ('file', models.FileField(upload_to='upload/files/')),
                ('type', models.TextField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='app.Sample')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('STARTED', 'Started'), ('ONGOING', 'On going'), ('ENDED', 'Finished')], max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='user_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sample',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='app.Project'),
        ),
    ]