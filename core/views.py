from multiprocessing import context
from django.shortcuts import render
from news.models import News
from projects.models import Projects

# Create your views here.


def home(request):
    news = News.objects.all().order_by('-id')[0:3]
    projects = Projects.objects.all().order_by('-id')[0:3]

    context = {
        'navbar': 'home_page',
        'news' : news,
        'projects': projects
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {'navbar': 'about_page'})


def partners_and_customers(request):
    return render(request, 'partners-and-customers.html', {'navbar': 'partners_page'})
    

def services(request):
    return render(request, 'services.html', {'navbar': 'services_page'})