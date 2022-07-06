from django.shortcuts import render
from django.http import HttpResponse
from meat.format import gostformat
import json

def index(request):
    res=""
    if request.method == "POST":
        res=gostformat("book", (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                                request.POST.get('publish-year'), request.POST.get('page-number')))
        return render(request, 'index.html', {"result":res, "main_page_active":"", "user_input_active":"section-visible",
                                              "main_button_active":"", "user_button_active":"active"})
    return render(request, 'index.html', {"main_page_active":"section-visible", "main_button_active":"active"})