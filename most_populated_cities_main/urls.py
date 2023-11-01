from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'most_populated_cities_main'

urlpatterns = [
    path('', views.city_page, name='cities'),
    path('countries', views.country_page, name='countries'),

]
