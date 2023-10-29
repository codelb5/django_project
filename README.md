# django_project

### we have initialized the project by creating an virtual environment and installing django in it.


### create a django project
```django-admin startproject <project_name>```

### to start the server
- go to the django project folder
```python manage.py runserver```
- the server will automatically refresh , for all the changes we make in the files

### create an app named `blog`
- in django each app is an individual instance, we can transfer any app from one project to other if we want.
```python manage.py startapp <app_name>```
- we already have our main app same as our project name.

### created urls.py inside blog app to navigate our webpage

### routed our blog app urls with main app urls

### updated the setings.py with blog apps.py config

### added html template to our blog webpage, home and about

### created posts in home page

### added base.html
- this file holds the base template for all our webpages
- we extended this template to our home page and about page.
- this gives us the advantage to make changes to the base template from a single file itself.
- the other web pages will have only the contents specific to that page.

# added sample bootstrap for styling our webpages