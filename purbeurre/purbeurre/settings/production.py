from .import *

SECRET_KEY ="?_Xd'_H}VP[U:-^36$IoK:y\x0c"
DEBUG= False
ALLOWED_HOSTS = ['157.245.72.19']

DATABASES ={
        'default': {
            'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
            'NAME': 'purbeurre', # le nom de notre base de données créée précédemment
            'USER': 'mickael', # attention : remplacez par votre nom d'utilisateur !!
            'PASSWORD': 'Lyteemo5',
            'HOST': '',
            'PORT': '5432',
        }
}

