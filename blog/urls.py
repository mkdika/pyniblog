from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:permalink>', views.post, name='post'),
    path('posts/<str:permalink>/addcomment', views.addcomment, name='addcomment'),
    path('posts/<str:search_by>/<str:id>', views.search, name='search'),
    path('about', views.about, name='about'),
    path('archives/<str:mode>', views.archive, name='archive'),
    path('archives/<str:mode>', views.archive, name='archive'),
]
