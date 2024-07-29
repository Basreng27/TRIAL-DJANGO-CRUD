from django.urls import path
from . import views

urlpatterns = [
    path('genre/', views.genre_list, name='genre_list'),
    path('genre_create/', views.genre_create, name='genre_create'),
    path('genre_update/<int:id>/', views.genre_create, name='genre_update'),
    path('genre_delete/<int:id>', views.genre_delete, name='genre_delete'),
    path('comic/', views.comic_list, name='comic_list'),
    path('comic_create/', views.comic_create, name='comic_create'),
    path('comic_update/<int:id>/', views.comic_create, name='comic_update'),
    path('comic_delete/<int:id>', views.comic_delete, name='comic_delete'),
    path('', views.default_page, name='default_page'),
]