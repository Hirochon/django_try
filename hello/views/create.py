from django.shortcuts import render
from django.views.generic import View
from ..forms import MemberForm
from ..models import Member

class addView(View):
    def __init__(self):
        self.params = {
            'title' : 'くりえいとぺえじ',
            'message' : 'はろはろクリエイト！！',
            'form' : MemberForm(),
        }

    def get(self, request, *args, **kwargs):
        return render(request, 'hello/create.html', self.params)
    
    def post(self, request, *args, **kwargs):
        obj = Member()
        member = MemberForm(request.POST, instance=obj)
        member.save()
        self.params['message'] = 'くりえいとに成功しますぃた。'
        self.params['form'] = MemberForm(request.POST)
        return render(request, 'hello/create.html', self.params)

add = addView.as_view()