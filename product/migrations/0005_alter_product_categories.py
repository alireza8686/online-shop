# Generated by Django 4.0.2 on 2022-03-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0004_productcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='category.Category', verbose_name='دسته بندی ها'),
        ),
    ]
