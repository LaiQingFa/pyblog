from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#定义响应函数index  类似于javaweb里面的controller
def index(request):
    return render(request,'index.html',{'key01':'value01'})

