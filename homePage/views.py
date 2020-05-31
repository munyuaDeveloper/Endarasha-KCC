from django.shortcuts import render


# Create your views here.

def home_page_view(request):
    context = {}

    return render(request, 'homePage/index.html', context)
