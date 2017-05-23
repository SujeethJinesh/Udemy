from django.conf.urls import url
from django.contrib import admin
from . import views

#to run the server do "python manage.py runserver"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about')
]
