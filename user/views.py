from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View

class UserView(View):
    def get(self, request, *args, **kwargs):
        user_model = get_user_model()
        users = user_model.objects.all()
        params = {
            'users' : users,
        }
        return render(request, 'user/user_home.html', params)