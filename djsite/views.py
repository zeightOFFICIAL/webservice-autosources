#views.py 0040

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from meat.format import format_book, format_article, format_websource
from meat.defaults import default_index, book_index, article_index, websource_index

def home_or_book_page(request):
    result=""
    if request.method == "POST":
        result=format_book(request)
        return render(request, 'index.html', book_index(result))
    return render(request, 'index.html', default_index())     

def article_page(request):
    result = ""
    if request.method == "POST":
        result=format_article(request)
        return render(request, 'index.html', article_index(result)) 
    else: 
        return render(request, 'index.html', default_index())                          

def websource_page(request):
    result = ""
    if request.method == "POST":
        result=format_websource(request)
        return render(request, "index.html", websource_index(result))
    else: 
        return render(request, 'index.html', default_index())     