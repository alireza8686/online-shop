# Generated by Django 3.2.7 on 2022-03-12 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('is_read', models.BooleanField(default=False, verbose_name='خوانده شده / نشده')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='وبلاگ')),
            ],
            options={
                'verbose_name': 'نظرات',
                'verbose_name_plural': 'نطرات کاربران ',
            },
        ),
    ]
