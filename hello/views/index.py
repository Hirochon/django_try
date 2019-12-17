from django.shortcuts import render
from django.views import View

## 関数を用いたviewの書き方
"""
def hello(request):
    params = {
        'title' : 'Index',
        'message' : 'Hello World!!',
    }
    return render(request, 'hello/index.html', params)
"""

## クラスを用いたviewの書き方
class HelloView(View):
    def get(self, request, *args, **kwargs):
        params = {
            'title' : 'Index',
            'message' : 'Hello Class World!!',
        }
        return render(request, 'hello/index.html', params)

hello = HelloView.as_view()