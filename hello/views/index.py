from django.shortcuts import render

def hello(request):
    params = {
        'title' : 'Index',
        'message' : 'Hello World!!',
    }
    return render(request, 'base.html', params)