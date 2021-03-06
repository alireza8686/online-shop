# Generated by Django 3.2.7 on 2022-03-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توصیحات')),
                ('author', models.CharField(max_length=200, verbose_name='نام نویسنده')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='تصویر')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='زمان انتشار')),
                ('is_published', models.BooleanField(default=False, verbose_name='منتشر شود / نشود')),
                ('view', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
            ],
            options={
                'verbose_name': 'بلاگ',
                'verbose_name_plural': 'بلاگ ها',
            },
        ),
    ]
