from django.shortcuts import render


# Create your views here.

def news_page_view(request):
    return render(request, 'newsPage/news.html', {})
