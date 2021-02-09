import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Url

def index(request):
    return render(request, 'index.html')

def createUrl(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        
        data = Url(url=url, uuid=uid)
        data.save()
        return HttpResponse(uid)

def go(request, pk):
    destination = Url.objects.get(uuid=pk)
    return redirect(destination.url)