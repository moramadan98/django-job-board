# Generated by Django 3.2.5 on 2021-07-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_coveletter_apply_job_coverletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='apply'),
        ),
    ]
