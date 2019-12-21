from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url

def index(request):
    print("INDEX")
    return render(request, 'index.html')

def shorten(request):
    print("SHORTED")
    original_url = request.POST.get('url')

    import uuid 
    little_url = str(uuid.uuid4().hex[:6])

    Url.objects.create(original=original_url, little=little_url)

    return HttpResponse('lttl:8000/' + little_url)
    

def lengthen(request):
    print("LENGTHEN")
    absolute_url = request.build_absolute_uri()
    little_url = absolute_url[len(absolute_url)-6:]

    original_url = Url.objects.filter(little=little_url)
    if len(original_url) != 1:
        return render(request, 'not_found.html')
    
    original_url = original_url[0].original

    if original_url[0:7] != 'http://' and original_url[0:8] != 'https://':
        original_url = 'http://' + original_url

    return redirect(original_url)