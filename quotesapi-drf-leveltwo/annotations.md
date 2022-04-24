-Useful steps/commands:
- Creating a virtual environment for python3:
    - python3 -m venv venv
    - source venv/bin/activate
- Start a django project on terminal
    - pip install django
    - pip install djangorestframework
    - pip freeze > requirements.txt
    - django-admin startproject newsapi
- Start a django project with docker
    - docker build .
    - docker-compose build
    - docker-compose run app sh -c "django-admin startproject quotesapi ."
    - docker-compose run app sh -c "python manage.py startapp quotes"
        - add 'ebooks' and 'rest_framework' to INSTALLED_APPS on settings.py
- After build a model:
    - register models in admin.py
    - docker-compose run app sh -c "python manage.py makemigrations"
    - docker-compose run app sh -c "python manage.py migrate"

    
- Create an admin:
    - docker-compose run app sh -c "python manage.py createsuperuser"
    
- docker-compose run app sh -c "python manage.py test && flake8"