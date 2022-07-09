from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from meat.format import gostformat

def home_or_output_book(request):
    res=""
    if request.method == "POST":
        res=gostformat("book", (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                                    request.POST.get('publish-year'), request.POST.get('page-number')))
        return render(request, 'index.html',{
                                            "result":res, "result2":"", "result3":"", 
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"form-visible", "book_button_active":"user-input-active",
                                            "article_form_visible":"", "article_button_active":"",
                                            "resource_form_visible":"", "resource_button_active":""
                                            })
    return render(request, 'index.html', {
                                          "result":"", "result2":"", "result3":"", 
                                          "main_page_active":"section-visible", "user_input_active":"",
                                          "main_button_active":"active", "user_button_active":"",
                                          "book_form_visible":"form-visible", "book_button_active":"user-input-active",
                                         })     

def index_1(request):
    res = ""
    if request.method == "POST":
        res=gostformat("article", (request.POST.get('author-surname'), request.POST.get('article-name'), request.POST.get('magazine-name'),
                                    request.POST.get('article-publish-year'), request.POST.get('magazine-number'), 
                                    request.POST.get('magazine-article-number')))
        return render(request, 'index.html',{
                                            "result":"", "result2":res, "result3":"",
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"", "book_button_active":"",
                                            "article_form_visible":"form-visible", "article_button_active":"user-input-active",
                                            "resource_form_visible":"", "resource_button_active":""
                                            }) 
    else: 
            return render(request, 'index.html', {
                                          "result":"", "result2":"", "result3":"", 
                                          "main_page_active":"section-visible", "user_input_active":"",
                                          "main_button_active":"active", "user_button_active":"",
                                          "book_form_visible":"form-visible", "book_button_active":"user-input-active",
                                         })                        

def index_2(request):
    res = ""
    if request.method == "POST":
        res=gostformat("webresource", (request.POST.get('resource-author'), request.POST.get('resource-name'), request.POST.get('resource-link'),
                                           request.POST.get('visit-date')))
        return render(request, "index.html",{
                                            "result":"", "result2":"", "result3":res,
                                            "main_page_active":"", "user_input_active":"section-visible",
                                            "main_button_active":"", "user_button_active":"active",
                                            "book_form_visible":"", "book_button_active":"",
                                            "article_form_visible":"", "article_button_active":"",
                                            "resource_form_visible":"form-visible", "resource_button_active":"user-input-active"
                                            })
    else: 
            return render(request, 'index.html', {
                                          "result":"", "result2":"", "result3":"", 
                                          "main_page_active":"section-visible", "user_input_active":"",
                                          "main_button_active":"active", "user_button_active":"",
                                          "book_form_visible":"form-visible", "book_button_active":"user-input-active"
                                         })      