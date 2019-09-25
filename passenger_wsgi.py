# -*- coding: utf-8 -*-
from django.core.wsgi import get_wsgi_application
import os
import sys
sys.path.insert(
    0, '/var/www/u0535492/data/www/todo.dev-pogodin.ru/TodoApp')
sys.path.insert(
    1, '/var/www/u0535492/data/todoappenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'TodoApp.settings'
application = get_wsgi_application()
