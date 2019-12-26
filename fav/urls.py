from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateFavoriteView.as_view(), name='fav_create'),
]