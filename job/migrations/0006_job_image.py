# Generated by Django 5.0 on 2024-09-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
