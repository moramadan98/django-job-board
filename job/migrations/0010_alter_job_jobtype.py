# Generated by Django 3.2.5 on 2021-07-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20210728_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobtype',
            field=models.CharField(choices=[('', 'Please select one'), ('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remotly', 'Remotly')], max_length=100),
        ),
    ]
