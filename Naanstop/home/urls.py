from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load-more/', views.load_more_posts, name='load_more_posts'),
]
