# Generated by Django 2.2 on 2020-05-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0003_auto_20200507_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='rating',
            field=models.IntegerField(),
        ),
    ]