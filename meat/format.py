"""
    Webservice autosources. Generator for sources string according to GOST. 
    Copyright (C) 2022-2023  Artemii Saganenko, Alexander Kuksin, Nikita Markin, Daniil Kurbanov
"""


#format.py 0045


"""
resource stack:
    book:
    {
        author,
        title,
        publisher,
        publish date,
        amount of pages
    }
    article
    {
        author,
        article title,
        magazine title,
        publish date,
        number of issue,
        number of article
    }
    web-resource
    {
        site author,
        title of page or article,
        reference,
        date of visit
    }
"""

def gostformat(resource_type, resource_stack):
    result = ""
    if resource_type == "book":
        if len(resource_stack) != 0:
            resource_stack_list = resource_stack[0].split(", ")
            print(resource_stack_list)
            if len(resource_stack_list) == 0:
                result = "{0}. - {1}, {2}. - {3} c.".format(resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4])
            elif len(resource_stack_list) == 1:
                result = "{0} {1}. - {2}, {3}. - {4} c.".format(resource_stack_list[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4])
            elif len(resource_stack_list) >= 2:
                result = "{0} {1} / ".format(resource_stack_list[0],resource_stack[1])
                for author_index in range(0, len(resource_stack_list)):
                    if author_index == len(resource_stack_list)-1:
                        result += "{0} ".format(resource_stack_list[author_index])
                    else:
                        result += "{0}, ".format(resource_stack_list[author_index])
                result += "- {0}, {1}. - {2} c.".format(resource_stack[2], resource_stack[3], resource_stack[4])
    elif resource_type == "article":
        if len(resource_stack) != 0:
            result = "{0} {1} // {2}. - {3}. - {4}. - С. {5}.".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4],resource_stack[5])
    elif resource_type == "webresource":
        if len(resource_stack) != 0:
            result = "{0} {1} [Электронный ресурс]. URL:{2} (дата обращения: {3})".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3])
    return result

def format_book(request):
    result = gostformat("book",(
                                request.POST.get('surname'), 
                                request.POST.get('book-name'), 
                                request.POST.get('publish-name'),
                                request.POST.get('publish-year'), 
                                request.POST.get('page-number')
                               ))
    return result

def format_article(request):
    result = gostformat("article", (
                                    request.POST.get('author-surname'), 
                                    request.POST.get('article-name'), 
                                    request.POST.get('magazine-name'),
                                    request.POST.get('article-publish-year'), 
                                    request.POST.get('magazine-number'),
                                    request.POST.get('magazine-article-number')
                                   ))
    return result

def format_websource(request):
    result = gostformat("webresource", (
                                        request.POST.get('resource-author'), 
                                        request.POST.get('resource-name'), 
                                        request.POST.get('resource-link'),
                                        request.POST.get('visit-date')
                                       ))
    return result
    