def gostformat(resource_type, resource_stack):
    result = ""
    if resource_type == "book":
        if len(resource_stack) != 0:
            result = "{0} {1}. - {2}, {3}. - {4} c.".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4])
    elif resource_type == "article":
        if len(resource_stack) != 0:
            result = "{0} {1} // {2}. - {3}. - {4}. - С. {5}.".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4],resource_stack[5])
    elif resource_type == "webresource":
        if len(resource_stack) != 0:
            result = "{0} {1} [Электронный ресурс]. URL:{2} (дата обращения: {3})".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3])
    return result

def book(request):
    res = gostformat("book",
                     (request.POST.get('surname'), request.POST.get('book-name'), request.POST.get('publish-name'),
                      request.POST.get('publish-year'), request.POST.get('page-number')))
    return res

def article(request):
    res = gostformat("article", (
    request.POST.get('author-surname'), request.POST.get('article-name'), request.POST.get('magazine-name'),
    request.POST.get('article-publish-year'), request.POST.get('magazine-number'),
    request.POST.get('magazine-article-number')))
    return res

def webresource(request):
    res = gostformat("webresource", (
    request.POST.get('resource-author'), request.POST.get('resource-name'), request.POST.get('resource-link'),
    request.POST.get('visit-date')))
    return res



