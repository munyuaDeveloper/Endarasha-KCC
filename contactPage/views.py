from django.shortcuts import render


# Create your views here.

def contact_page_view(request):
    return render(request, 'contactPage/contact.html', {})
