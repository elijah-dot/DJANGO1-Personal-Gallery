from django.urls import path
from . import views


urlpatterns =[
    path('', views.gallery, name='gallery'),
    path('photo/<pk>', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    # path('search/', views.search_category, name='search'),
    # path('delete/<category>', views.delete, name='delete'),
]
