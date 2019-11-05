# Django 2.0 Skeleton 

### How to run project
1. Clone repo: `git clone https://github.com/dlyapun/django_skeleton.git`
2. Enter to repo: `cd django_skeleton`
3. Create virtual environment: `virtualenv -p python3 venv`.
4. Activate virtual environment: `source venv/bin/activate`.
5. Install requirements: `pip3 install -r requirements.txt`.
6. Run migrations: `python3 manage.py migrate`.
6. Run server: `python3 manage.py runserver`.

### Local settings

```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

```
