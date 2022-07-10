def gostformat(resource_type, resource_stack):
    result = ""
    if resource_type == "book":
        if len(resource_stack) != 0:
            result += resource_stack[0]
            result += " " + resource_stack[1]
            result += ". – " + resource_stack[2] + ", " + resource_stack[3] + ". - "
            result += resource_stack[4] + " с."
    elif resource_type == "article":
        if len(resource_stack) != 0:
            result += resource_stack[0]
            result += " " + resource_stack[1]
            result += " // " + resource_stack[2] + ". - " + resource_stack[3] + ". - "
            result += resource_stack[4] + ". - С. " + resource_stack[5] + "."
    elif resource_type == "webresource":
        if len(resource_stack) != 0:
            result += resource_stack[0]
            result += " " + resource_stack[1] + " [Электронный ресурс]. URL:"
            result += resource_stack[2] + " (дата обращения: " + resource_stack[3] + ")"
    return result

def format_book(request):
    result = gostformat("book",
                     (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                      request.POST.get('publish-year'), request.POST.get('page-number')))
    return result

def format_article(request):
    result = gostformat("article", (
    request.POST.get('author-surname'), request.POST.get('article-name'), request.POST.get('magazine-name'),
    request.POST.get('article-publish-year'), request.POST.get('magazine-number'),
    request.POST.get('magazine-article-number')))
    return result

def format_websource(request):
    result = gostformat("webresource", (
    request.POST.get('resource-author'), request.POST.get('resource-name'), request.POST.get('resource-link'),
    request.POST.get('visit-date')))
    return result