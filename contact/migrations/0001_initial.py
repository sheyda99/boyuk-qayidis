# Generated by Django 4.1.1 on 2022-11-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Ad Soyad')),
                ('number', models.CharField(max_length=20, verbose_name='Telefon nömrəsi')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('subject', models.CharField(max_length=150, verbose_name='Mövzu')),
                ('messege', models.TextField(max_length=2000, verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
