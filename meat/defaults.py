def default_index():
    return  {
            "result":"", "result2":"", "result3":"", 
            "main_page_active":"section-visible", "user_input_active":"",
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