# Generated by Django 3.2.5 on 2021-07-28 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_apply_job_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_job',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.job'),
            preserve_default=False,
        ),
    ]