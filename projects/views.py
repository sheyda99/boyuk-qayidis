from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .models import Projects

# Create your views here.

def projects(request):
    projects = Projects.objects.all().order_by('-id')
   
    page_num = request.GET.get('page', 1)

    paginator = Paginator(projects, 6) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'navbar': 'projects_page',
        'page_obj': page_obj,
        'projects': page_obj.object_list
    }


    return render(request, 'projects.html', context)

def projects_details(request, slug):
    projects = get_object_or_404(Projects, slug = slug)

    context = {
        'navbar': 'projects_page',
        'projects' : projects
    }

    return render(request, 'project-details.html', context)