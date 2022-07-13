#default.py 0040

"""
This file indicates a set of values for HTML.
Since we have only one HTML, changing values inside is a practical necessity. 
Here there are four pre-arranged sets of values for default page (homepage) book, article, web-resource pages. 
Upon function call (by button pressing) we re-render pages with specific for the case set of values.
"""

def default_index():
    return  {
            "result":"", "result2":"", "result3":"", 
            "user_input_active":"section-visible",
            "main_button_active":"active", "user_button_active":"",
            "book_form_visible":"form-visible", "book_button_active":"user-input-active",
            }

def book_index(value):
    return  {
            "result":value, "result2":"", "result3":"", 
            "main_page_active":"", "user_input_active":"section-visible",
            "main_button_active":"", "user_button_active":"active",
            "book_form_visible":"form-visible", "book_button_active":"user-input-active",
            "article_form_visible":"", "article_button_active":"",
            "resource_form_visible":"", "resource_button_active":""
            }

def article_index(value):
    return  {
            "result":"", "result2":value, "result3":"",
            "main_page_active":"", "user_input_active":"section-visible",
            "main_button_active":"", "user_button_active":"active",
            "book_form_visible":"", "book_button_active":"",
            "article_form_visible":"form-visible", "article_button_active":"user-input-active",
            "resource_form_visible":"", "resource_button_active":""
            }

def websource_index(value):
    return  {
            "result":"", "result2":"", "result3":value,
            "main_page_active":"", "user_input_active":"section-visible",
            "main_button_active":"", "user_button_active":"active",
            "book_form_visible":"", "book_button_active":"",
            "article_form_visible":"", "article_button_active":"",
            "resource_form_visible":"form-visible", "resource_button_active":"user-input-active"
            }