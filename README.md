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

#### 3.3 Creating CustomUser by Replacing Default User and create database

        (venv39225) λ python manage.py makemigrations
        (venv39225) λ python manage.py migrate


        (venv39225) λ python manage.py sqlmigrate users 0001
        BEGIN;
        --
        -- Create model MyCustomUser
        --        
        CREATE TABLE "users_mycustomuser" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                "password" varchar(128) NOT NULL, 
                "last_login" datetime NULL, 
                "is_superuser" bool NOT NULL, 
                "username" varchar(150) NOT NULL UNIQUE, 
                "first_name" varchar(30) NOT NULL, 
                "last_name" varchar(150) NOT NULL, 
                "email" varchar(254) NOT NULL, 
                "is_staff" bool NOT NULL, 
                "is_active" bool NOT NULL, 
                "date_joined" datetime NOT NULL
        );

        CREATE TABLE "users_mycustomuser_groups" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "mycustomuser_id" integer NOT NULL REFERENCES "users_mycustomuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
        CREATE TABLE "users_mycustomuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "mycustomuser_id" integer NOT NULL REFERENCES "users_mycustomuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
        CREATE UNIQUE INDEX "users_mycustomuser_groups_mycustomuser_id_group_id_4231390f_uniq" ON "users_mycustomuser_groups" ("mycustomuser_id", "group_id");
        CREATE INDEX "users_mycustomuser_groups_mycustomuser_id_9e5e8f14" ON "users_mycustomuser_groups" ("mycustomuser_id");
        CREATE INDEX "users_mycustomuser_groups_group_id_4348317b" ON "users_mycustomuser_groups" ("group_id");
        CREATE UNIQUE INDEX "users_mycustomuser_user_permissions_mycustomuser_id_permission_id_23565a0d_uniq" ON "users_mycustomuser_user_permissions" ("mycustomuser_id", "permission_id");
        CREATE INDEX "users_mycustomuser_user_permissions_mycustomuser_id_3edfb74d" ON "users_mycustomuser_user_permissions" ("mycustomuser_id");
        CREATE INDEX "users_mycustomuser_user_permissions_permission_id_ed16a8b3" ON "users_mycustomuser_user_permissions" ("permission_id");
        COMMIT;
























































































































































































































































