# Generated by Django 4.2.7 on 2023-11-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(),
        ),
    ]