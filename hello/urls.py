from django.urls import path
from .views import index,create,edit

urlpatterns = [
    path('', index.hello, name='index'),
    path('create/', create.add, name='create'),
    path('morecreate/', create.addmore, name='morecreate'),
    path('edit/<int:num>', edit.edit, name='edit'),
]