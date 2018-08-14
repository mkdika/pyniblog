from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:permalink>', views.post, name='post'),
    path('posts/<str:search_by>/<str:id>', views.search, name='search'),
    path('about', views.about, name='about'),
]
