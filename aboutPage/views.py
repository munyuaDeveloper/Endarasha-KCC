from django.shortcuts import render


# Create your views here.

def about_page_view(request):
    context = {}

    return render(request, 'aboutPage/about.html', context)
