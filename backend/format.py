"""
format.py
PyCharm 2022.1.3
Python 3.9
"""
"""
type =
book or article or web-source
source stack = 
{
author and initials,    -
title,                  -
issue number,           -
city of issue,          -
name of publisher,      -
date of issue,          -
amount of pages         -
}
"""


def gostformat(resource_type, resource_stack):
    result = ""
    if resource_type == "book":
        if len(resource_stack) != 0:
            result += resource_stack[0]
            result += " " + resource_stack[1]
            result += ". – " + resource_stack[2] + ", " + resource_stack[3] + ". - "
            result += resource_stack[4] + " с."
    return result
