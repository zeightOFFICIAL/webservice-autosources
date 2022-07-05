"""
Resources auto-generation and formatting
for Article, book or web-source
SPBSUT
Saganenko A.V
Kuksin A.A
Maksimenko S.O
Markin N.
Scherbakova N.
Ibragimova A.
main.py
    - format.py
    - parser.py
    - bridge.py
    - readdoc.py
PyCharm 2022.1.3
Python 3.9
"""

import format


def main():

    print(format.gostformat("book", ("Glinka A.A.", "Lovers and Dungeons", "DolbitNorm", "2020", "431")))


if __name__ == "__main__":
    main()
