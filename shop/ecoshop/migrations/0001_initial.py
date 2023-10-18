# Generated by Django 4.2.5 on 2023-10-18 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(default='perfect products', max_length=100)),
                ('price', models.FloatField()),
                ('amount', models.PositiveIntegerField()),
                ('delivery_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('FR', 'Fruit'), ('VG', 'Vegetable'), ('ML', 'Milk products'), ('MT', 'Meat'), ('TC', 'Tea and coffee'), ('FS', 'Fish'), ('AL', 'Alcohol')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecoshop.person')),
                ('personal_discont', models.FloatField(null=True)),
            ],
            bases=('ecoshop.person',),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecoshop.person')),
                ('inn', models.PositiveIntegerField(null=True)),
            ],
            bases=('ecoshop.person',),
        ),
        migrations.CreateModel(
            name='ProductsReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(default='default review', max_length=300)),
                ('author', models.CharField(max_length=30)),
                ('reviews_time', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoshop.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='product',
            field=models.ManyToManyField(to='ecoshop.product'),
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.PositiveIntegerField()),
                ('passport_series', models.CharField(max_length=5)),
                ('person', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoshop.person')),
            ],
        ),
        migrations.CreateModel(
            name='VendorReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(default='default review', max_length=300)),
                ('author', models.CharField(max_length=30)),
                ('reviews_time', models.DateField(auto_now_add=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoshop.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipperReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(default='default review', max_length=300)),
                ('author', models.CharField(max_length=30)),
                ('reviews_time', models.DateField(auto_now_add=True)),
                ('shipper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecoshop.shipper')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
