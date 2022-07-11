#format.py 0031

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
            if len(resource_stack_list) == 1:
                result = "{0} {1}. - {2}, {3}. - {4} c.".format(resource_stack_list[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4])
            if len(resource_stack_list) >= 2:
                result = "{0} {1} / ".format(resource_stack_list[0],resource_stack[1])
                for i in range(0, len(resource_stack_list)):
                    if i != len(resource_stack_list)-1:
                        result += "{0}, ".format(resource_stack_list[i])
                    else:
                        result += "{0} ".format(resource_stack_list[i])
                result += "- {0}, {1}. - {2} c.".format(resource_stack[2], resource_stack[3], resource_stack[4])


    elif resource_type == "article":
        if len(resource_stack) != 0:
            result = "{0} {1} // {2}. - {3}. - {4}. - С. {5}.".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3],resource_stack[4],resource_stack[5])
    elif resource_type == "webresource":
        if len(resource_stack) != 0:
            result = "{0} {1} [Электронный ресурс]. URL:{2} (дата обращения: {3})".format(resource_stack[0],resource_stack[1],resource_stack[2],resource_stack[3])
    return result
