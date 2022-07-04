"""
format.py
PyCharm 2022.1.3
Python 3.9
"""


class GOST71:
    def __init__(self, source_type, source_stack):
        self.source_type = source_type
        self.source_stack = source_stack

    def __str__(self):
        print(self.source_type + "\n" + self.source_stack)
