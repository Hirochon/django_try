from django.urls import path
from .views import index,create

urlpatterns = [
    path('', index.hello, name='index'),
    path('create/', create.add, name='create'),
]