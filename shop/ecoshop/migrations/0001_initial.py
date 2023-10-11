# Generated by Django 4.2.5 on 2023-10-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(default='perfect products', max_length=100)),
                ('price', models.FloatField()),
                ('vendor', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField()),
                ('delivery_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('FR', 'Fruit'), ('VG', 'Vegetable'), ('ML', 'Milk products'), ('MT', 'Meat'), ('TC', 'Tea and coffee'), ('FS', 'Fish'), ('AL', 'Alcohol')], max_length=2)),
            ],
        ),
    ]
