from django.urls import path
from . import views


urlpatterns = [
    path('', views.favesongs_home, name='favesongs_home'),
    path('create/', views.favesongs_create, name='favesongs_create'),
    path('thelist/', views.favesongs_thelist, name='favesongs_thelist'),
    path('<int:pk>/details/', views.favesongs_details, name='favesongs_details'),
    path('<int:pk>/edit/', views.favesongs_edit, name='favesongs_edit'),
    path('<int:pk>/delete/', views.favesongs_delete, name='favesongs_delete'),
]