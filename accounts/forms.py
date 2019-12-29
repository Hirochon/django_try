from allauth.account.forms import SignupForm
from django import forms

class MyCustomSignupForm(SignupForm):
    username = forms.CharField(label='ユーザID', required=True, help_text='※必須',
                                widget=forms.TextInput(attrs={'placeholder':'taro'}))
    email = forms.EmailField(label='メールアドレス', required=True, help_text='※必須',
                                widget=forms.TextInput(attrs={'placeholder':'taro@example.com'}))
    age = forms.IntegerField(label='年齢', required=True, help_text='※必須', min_value=0, max_value=150)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user