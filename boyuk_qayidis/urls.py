"""boyuk_qayidis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from core.views import (
    home,
    about,
    partners_and_customers,
    services,
)

from news.views import (
    news,
    news_details
)

from projects.views import (
    projects,
    projects_details
)

from contact.views import (
    contact
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('partners_and_customers/', partners_and_customers, name='partners'),
    path('services/', services, name='services'),
    path('news/', news, name='news'),
    path('news_detail/<slug:slug>/', news_details, name='news_detail'),
    path('projects/', projects, name='projects'),
    path('projects_detail/<slug:slug>/', projects_details, name='projects_detail'),
    path('contact/', contact, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

