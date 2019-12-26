from django.urls import path
from .views import createfav

urlpatterns = [
    path('', createfav, name='fav_create'),
]