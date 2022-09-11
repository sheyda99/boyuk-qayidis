from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .models import News

# Create your views here.

def news(request):
    news = News.objects.all().order_by('-id')
   
    page_num = request.GET.get('page', 1)

    paginator = Paginator(news, 3) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'navbar': 'news_page',
        'page_obj': page_obj,
        'news': page_obj.object_list
    }

    # print(news.title)
    return render(request, 'news.html', context)

def news_details(request, slug):
    news = get_object_or_404(News, slug = slug)

    context = {
        'navbar': 'news_page',
        'news' : news
    }

    return render(request, 'news-details.html', context)