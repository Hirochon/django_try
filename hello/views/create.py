from django.shortcuts import render, redirect
from django.views.generic import View
from ..forms import MemberForm, GroupForm
from ..models import Member, Group

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
        return redirect(to='/hello/morecreate/')

class addmoreView(View):
    def __init__(self):
        self.params = {
            'title' : 'ぐるうぷくりえいとぺえじ',
            'message' : 'グループを選択してください！',
            'form' : GroupForm(),
        }

    def get(self, request, *args, **kwargs):
        return render(request, 'hello/morecreate.html', self.params)

    def post(self, request, *args, **kwargs):
        obj = Group()
        group = GroupForm(request.POST, instance=obj)
        group.save()
        return redirect(to='/hello')

add = addView.as_view()
addmore = addmoreView.as_view()