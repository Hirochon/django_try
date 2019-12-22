from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # self.objectにsave()されたユーザオブジェクトが格納される
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid