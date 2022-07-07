from django.shortcuts import render
from django.http import HttpResponse
from meat.format import gostformat

def index(request):
    res=""
    if request.method == "POST":
        if request.POST.get("type") == "type_book":
            res=gostformat("book", (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                                    request.POST.get('publish-year'), request.POST.get('page-number')))
            return render(request, 'index.html', {
                                                 "result":res, "result2":"", "result3":"", 
                                                 "main_page_active":"", "user_input_active":"section-visible",
                                                 "main_button_active":"", "user_button_active":"active"
                                                 })
        elif request.POST.get("type") == "type_article":
            res=gostformat("article", (request.POST.get('author-surname'), request.POST.get('article-name'), request.POST.get('magazine-name'),
                                    request.POST.get('article-publish-year'), request.POST.get('magazine-number'), 
                                    request.POST.get('magazine-article-number')))
            return render(request, 'index.html', {
                                                 "result":"", "result2":res, "result3":"",
                                                 "main_page_active":"", "user_input_active":"section-visible",
                                                 "main_button_active":"", "user_button_active":"active",
                                                 })
        elif request.POST.get("type") == "type_source":
            res=gostformat("webresource", (request.POST.get('resource-author'), request.POST.get('resource-name'), request.POST.get('resource-link'),
                                           request.POST.get('visit-date')))
            return render(request, "index.html", {
                                                 "result":"", "result2":"", "result3":res,
                                                 "main_page_active":"", "user_input_active":"section-visible",
                                                 "main_button_active":"", "user_button_active":"active",
                                                 })
    return render(request, 'index.html', {"main_page_active":"section-visible", "main_button_active":"active"})