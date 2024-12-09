"""
WSGI config for cryptotracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from typeguard import install_import_hook

install_import_hook('cryptotracker')
install_import_hook('tracker')
install_import_hook('portfolio')

import tracker
from tracker import portfolio
import cryptotracker

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptotracker.settings')

application = get_wsgi_application()
