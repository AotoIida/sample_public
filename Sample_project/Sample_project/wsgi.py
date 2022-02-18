"""
WSGI config for Sample_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys #mod_wsgi

from django.core.wsgi import get_wsgi_application

#mod_wsgi設定
sys.path.append('/home/ec2-user/Django/sample_public/Sample_project')
sys.path.append('/home/ec2-user/Django/sample_public/Sample_project/Sample_project')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sample_project.settings')

application = get_wsgi_application()

