# Generated by Django 3.1.4 on 2020-12-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test3app', '0004_auto_20201224_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_table',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('O', 'Others'), ('M', 'Male')], max_length=100),
        ),
    ]
