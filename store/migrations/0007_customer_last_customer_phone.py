# Generated by Django 4.0.4 on 2022-07-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
