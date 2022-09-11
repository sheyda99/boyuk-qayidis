# Generated by Django 4.1.1 on 2022-09-10 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/news', verbose_name='Əsas Şəkil')),
                ('title', models.CharField(max_length=256, verbose_name='Başlıq')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil4')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil5')),
                ('description1', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Məzmun1')),
                ('description2', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Məzmun2')),
                ('description3', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Məzmun3')),
                ('description4', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Məzmun4')),
                ('description5', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Məzmun5')),
                ('slug', models.SlugField(editable=False, max_length=110, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
