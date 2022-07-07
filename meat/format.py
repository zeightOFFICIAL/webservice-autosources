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

## ("book", ("Glinka A.A.", "Lovers and Dungeons", "DolbitNorm", "2020", "431"))
## ("article", ("Glinka A.A.", "Lovers and Dungeons", "DolbitNorm", "2020", "№228" "100-121"))
## ("webresource", ("Glinka A.A.", "Lovers and Dungeons", "http://DolbitNorm", "05.05.2020""))
    return result
