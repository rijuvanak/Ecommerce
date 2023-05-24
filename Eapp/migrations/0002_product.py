# Generated by Django 3.2.16 on 2023-05-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]