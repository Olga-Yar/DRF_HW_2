# Generated by Django 4.2.1 on 2023-08-21 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Course/', verbose_name='превью')),
                ('about', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('student', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='студент')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=50)),
                ('payment_sum', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Course/', verbose_name='превью')),
                ('about', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('url', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
                ('course', models.ManyToManyField(blank=True, null=True, to='study.course')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
