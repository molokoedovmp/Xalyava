# Generated by Django 5.0.4 on 2024-05-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/products/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]