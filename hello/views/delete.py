from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import Member

class deleteView(View):
    def get(self, request, num, *args, **kwargs):
        member = Member.objects.get(id=num)
        params = {
            'title' : 'でりいとぺえじ',
            'message' : '※本当に削除してええんか？(小藪)',
            'items' : member,
            'id' : num,
        }
        return render(request, 'hello/delete.html', params)
        
    def post(self, request, num, *args, **kwargs):
        member = Member.objects.get(id=num)
        member.delete()
        return redirect(to='/hello')

delete = deleteView.as_view()