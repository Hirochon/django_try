from django.shortcuts import render
from django.views.generic import View

class addView(View):
    def get(self, request, *args, **kwargs):
        params = {
            'title' : 'くりえいとぺえじ',
            'message' : 'はろはろクリエイト！！',
        }
        return render(request, 'hello/create.html', params)

add = addView.as_view()