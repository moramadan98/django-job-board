# Generated by Django 3.2.5 on 2021-07-27 23:10

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_img',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]