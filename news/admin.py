from django.contrib import admin
from .models import News


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description1', 'created_at', 'updated_at')
    list_filter = ('description1', 'created_at', 'updated_at')
    search_fields = ('description1', 'created_at', 'updated_at')

admin.site.register (News, NewsAdmin)