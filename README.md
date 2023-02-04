
# Autosources webservice

## Webservice - automatic generation of web, book, article sources according to GOST

### Authors: A.V. Saganenko, A.A. Kuksin, N.V. Markin, D. Kurbanov

#### Saint Petersburg State University of Telecommunications

### Description

The web service was created to facilitate the writing of documentation and reports. The main task of this service is automatic formatting of sources according to GOST. The project was implemented in two days during an internship by students with no web development experience whatsoever. The purpose of the development was to simplify the writing of any documentation, in the light of a large number of sources. With this service, the process of writing documentation has been dramatically simplified.

### Dev-stack

* HTML5
* CSS
* JavaScript
* Python3
* Django

### Launch conditions

Be sure to have packages listed in requirements.txt installed. Use any IDE able to interpret Python code. Create .env file in which you should store SECRET_KEY (for example SECRET_KEY='4221'), it should be not visible during production. Launch from manage.py, settings in settings.py.

First launch from new machine

``` python3
python ./manage.py migrate
```

Launch server

``` python3
python ./manage.py runserver
```

### Package list

* Django is a framework (4.1.5, should be compatible with anything 4.0 .. 5.0)
* python-decouple to work with envs (version is tied to Django be careful, 3.7)

### Features

* Generate source according to GOST of next types of content:
*  * Book
*  * Article
*  * Web-resource
*  Convenient menu and easy navigation
*  Completely user-friendly
*  Deployable on most servers

### Contributors

* @SaharoK-Er404 - Team lead, python programmer, documentation
* @dabchinsky - Front-end lead, design
* @zeightOFFICIAL - Back-end lead, architecture, documentation
* @Kurbanov0 - Python programmer, architecture, concept
* @Mckzzz - Python programmer, concept

### Future scope

- Add string autogeneration from URL
- Add string autogeneration from file
