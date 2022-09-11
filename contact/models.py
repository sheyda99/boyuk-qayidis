from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Contact(models.Model):
    # information
    name = models.CharField('Ad Soyad', max_length = 20)
    number = models.CharField('Telefon nömrəsi', max_length = 20)
    email = models.EmailField('Email', max_length = 50)
    subject = models.CharField('Mövzu', max_length = 150)
    messege = models.CharField('Mesaj', max_length = 2000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name