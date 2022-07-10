from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from meat.format import gostformat,book,article,webresource


def home_or_output_book(request):
    res=""
    if request.method == "POST":
        res= book(request)
        return render(request, 'base3.html',{"result":res})
    return render(request, 'base2.html')

def index_1(request):
    res = ""
    if request.method == "POST":
        res=article(request)
        return render(request, 'base4.html',{"result2":res})

    return render(request, 'base2.html')

def index_2(request):
    res = ""
    if request.method == "POST":
        res=webresource(request)
        return render(request, "base5.html",{"result3":res})

    return render(request, 'base2.html')