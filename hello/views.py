from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return  render(request,'hello/index.html')
            #HttpResponse('<h1>Hello, World!</h1>')
def greet(request, name):
    from django.utils import timezone
    hour = timezone.localtime().hour
    return render(request,'hello/greet.html',{'name': name.title(), 'hour':hour})
            #HttpResponse(f'<h1>Hello, {name.title()}!</h1>')