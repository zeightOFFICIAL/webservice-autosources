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
class GOST():

    def __init__ (self, resource_type, resource_stack):
        self.resource_type = resource_type
        self.resource_stack = resource_stack
        self.result = ""
        self.format()

    def format(self):
        if self.resource_type == "book":
            if len(self.resource_stack) != 0:
                    self.result += self.resource_stack[0]
                    self.result += " " + self.resource_stack[1]
                    self.result += ". – " + self.resource_stack[2] + ", " + self.resource_stack[3] + ". -  "
                    self.result += self.resource_stack[4] + " с."
        print(self.result)