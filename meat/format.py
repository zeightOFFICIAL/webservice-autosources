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
