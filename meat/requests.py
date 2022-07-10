#requests.py 0031

from meat.format import gostformat

def book_request(request):
    result_string = gostformat("book", (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                                        request.POST.get('publish-year'), request.POST.get('page-number')))
    return result_string

def article_request(request):
    result_string = gostformat("article", (request.POST.get('author-surname'), request.POST.get('article-name'), request.POST.get('magazine-name'),
                                           request.POST.get('article-publish-year'), request.POST.get('magazine-number'),
                                           request.POST.get('magazine-article-number')))
    return result_string

def webresource_request(request):
    result_string = gostformat("webresource", (request.POST.get('resource-author'), request.POST.get('resource-name'), request.POST.get('resource-link'),
                                               request.POST.get('visit-date')))
    return result_string
