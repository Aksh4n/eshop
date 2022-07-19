# Generated by Django 4.0.4 on 2022-07-18 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price_before'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
