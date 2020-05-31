from django.contrib import admin
from django.urls import path

from account.views import my_account_view
from contactPage.views import contact_page_view
from homePage.views import home_page_view
from aboutPage.views import about_page_view
from newsPage.views import news_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('news/', news_page_view, name='news'),
    path('contact/', contact_page_view, name='contact'),
    path('account/', my_account_view, name='account'),
]
