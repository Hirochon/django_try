from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import FavoriteForm

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
        # モデルオブジェクトのsave()時にファイルがアップロードされる。
        favorite.save()
        return redirect(to='/fav')

createfav = CreateFavoriteView.as_view()