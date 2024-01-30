from django.urls import path
from . import views

urlpatterns = [
    path('dropdown', views.index, name='index'),
    path('fetch-state', views.fetch_state, name='fetch_state'),
    path('fetch-city', views.fetch_city, name='fetch_city'),
]
