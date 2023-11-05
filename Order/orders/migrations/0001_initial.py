# Generated by Django 4.2.7 on 2023-11-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField()),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_shipped', models.BooleanField(default=False)),
                ('order_quantity', models.PositiveIntegerField()),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
    ]