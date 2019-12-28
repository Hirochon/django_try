from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import FavoriteForm
from .models import Favorite

class CreateFavoriteView(LoginRequiredMixin, View):
    def __init__(self):
        self.template_name = 'fav/favorite_form.html'

    def get(self, request, *args, **kwargs):
        context = {'form':FavoriteForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FavoriteForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, self.template_name, {'form':form})

        favorite = form.save(commit=False)
        favorite.submitter = self.request.user
        favorite.save()
        return redirect(to='/fav')

class lookfavView(View):
    def get(self, request, *args, **kwargs):
        favorites = Favorite.objects.all().order_by('-id') 
        return render(request, 'fav/fav_look.html', {'favorites' : favorites})