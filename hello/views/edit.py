from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import Member
from ..forms import MemberForm

class editView(View):

    def get(self, request, num, *args, **kwargs):
        obj = Member.objects.get(id=num)
        form = MemberForm(instance=obj)
        params = {
            'title' : 'へんしゅうぺえじ',
            'message' : '編集したい内容を変えてね！',
            'form' : form,
            'id' : num,
        }
        return render(request, 'hello/edit.html', params)

    def post(self, request, num, *args, **kwargs):
        obj = Member.objects.get(id=num)
        member = MemberForm(request.POST, instance=obj)
        member.save()
        return redirect(to='/hello')

edit = editView.as_view()