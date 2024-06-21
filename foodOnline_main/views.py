from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Namaste Duniya')
    return render(request,'home.html')