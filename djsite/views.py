#views.py 0031

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from meat.requests import book_request, article_request, webresource_request

def home_index(request):
    result = ""
    if request.method == "POST":
        result=book_request(request)
        return render(request, 'book_page.html', {"result":result})
    return render(request, 'homepage.html')

def article_index(request):
    result = ""
    if request.method == "POST":
        result=article_request(request)
        return render(request, 'article_page.html', {"result2":result})
    return render(request, 'homepage.html')

def webresource_index(request):
    result = ""
    if request.method == "POST":
        result=webresource_request(request)
        return render(request, "webresource_page.html", {"result3":result})
    return render(request, 'homepage.html')
