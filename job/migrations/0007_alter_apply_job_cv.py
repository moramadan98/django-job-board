# Generated by Django 3.2.5 on 2021-07-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_remove_apply_job_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='cv',
            field=models.FileField(default=1, upload_to='apply'),
            preserve_default=False,
        ),
    ]
