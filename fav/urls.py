from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateFavoriteView.as_view(), name='fav_create'),
    path('', views.lookfavView.as_view(), name='fav_look'),
]