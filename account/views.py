from django.shortcuts import render


# Create your views here.

def my_account_view(request):
    return render(request, 'account/my_account.html', {})
