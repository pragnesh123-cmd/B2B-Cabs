# Generated by Django 4.0.3 on 2022-04-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_comfirmbooking_confirmbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='postbooking',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='postbooking',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
