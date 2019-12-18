from django import forms
from .models import Member, Group

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','age','sex']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['member','name']