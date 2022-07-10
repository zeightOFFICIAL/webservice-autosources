from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from meat.format import format_book, format_article, format_websource
from meat.defaults import default_index

def home_or_book_page(request):
    res=""
    if request.method == "POST":
        res=format_book(request)
        return render(request, 'index.html',{
                                            "result":res, "result2":"", "result3":"", 
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"form-visible", "book_button_active":"user-input-active",
                                            "article_form_visible":"", "article_button_active":"",
                                            "resource_form_visible":"", "resource_button_active":""
                                            })
    return render(request, 'index.html', default_index())     

def article_page(request):
    res = ""
    if request.method == "POST":
        res=format_article(request)
        return render(request, 'index.html',{
                                            "result":"", "result2":res, "result3":"",
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"", "book_button_active":"",
                                            "article_form_visible":"form-visible", "article_button_active":"user-input-active",
                                            "resource_form_visible":"", "resource_button_active":""
                                            }) 
    else: 
            return render(request, 'index.html', default_index())                          

def websource_page(request):
    res = ""
    if request.method == "POST":
        res=format_websource(request)
        return render(request, "index.html",{
                                            "result":"", "result2":"", "result3":res,
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"", "book_button_active":"",
                                            "article_form_visible":"", "article_button_active":"",
                                            "resource_form_visible":"form-visible", "resource_button_active":"user-input-active"
                                            })
    else: 
            return render(request, 'index.html', default_index())       