# Generated by Django 3.2.9 on 2021-11-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211125_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='prioritysubmission',
            name='currentStatus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prioritysubmission',
            name='dateCreated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prioritysubmission',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]