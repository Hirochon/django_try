from django.shortcuts import render
from django.views import View
from ..models import Member, Group

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
        members = Member.objects.all()
        groups = Group.objects.all()
        params = {
            'title' : 'Index',
            'message' : 'Hello Class World!!',
            'members' : members,
            'groups' : groups,
        }
        return render(request, 'hello/index.html', params)

hello = HelloView.as_view()