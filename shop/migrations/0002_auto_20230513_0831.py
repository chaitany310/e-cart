# Generated by Django 3.2.12 on 2023-05-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product',
            new_name='product_name',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.CharField(default='', max_length=200),
        ),
    ]