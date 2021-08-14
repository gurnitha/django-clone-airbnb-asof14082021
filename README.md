### CLONE AIRBNB USING DJANGO


#### Links to sources:

https://github.com/gurnitha/django-clone-airbnb-asof14082021
https://github.com/nomadcoders/airbnb-clone


#### --------------
#### 1 BASICS SETUP
#### --------------


#### 1.1 Create venv and install django v2.2.5

        new file:   .gitignore
        new file:   README.md

#### 1.2 Github repository

        modified:   README.md


#### ----------------
#### 2 DJANGO PROJECT
#### ----------------


#### 2.1 Create django project called 'config'

        (venv39225) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2 Modify settings.py file

        (venv39225) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py

#### 2.3 Setting up static and media files root and path

        (venv39225) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py


#### -----------
#### 3. USER APP
#### -----------


#### 3.1 Create a new app called 'apps/users'

        (venv39225) λ mkdir apps\users
        (venv39225) λ python manage.py startapp users apps/users

        modified:   README.md
        new file:   apps/users/__init__.py
        new file:   apps/users/admin.py
        new file:   apps/users/apps.py
        new file:   apps/users/migrations/__init__.py
        new file:   apps/users/models.py
        new file:   apps/users/tests.py
        new file:   apps/users/views.py       

#### 3.2 Register users app to the project 'settings.py' file

        (venv39225) λ python manage.py check
        System check identified no issues (0 silenced). 




























































































































































































































































