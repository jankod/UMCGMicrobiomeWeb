"""
WSGI config for UMCGMicrobiomeWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


from sys import platform
if platform == "linux" or platform == "linux2":
    sys.path.append('/home/tag/umcg_web/UMCGMicrobiomeWeb/UMCGMicrobiomeWeb')
    sys.path.append('/home/tag/umcg_web/UMCGMicrobiomeWeb')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UMCGMicrobiomeWeb.settings')

#sys.path.append('/home/django_projects/MyProject')

application = get_wsgi_application()
