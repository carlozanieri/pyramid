from os import environ
from pyramid.paster import get_app, setup_logging

environ = '/usr/bin/python3.9 '
environ['HGENCODING'] = 'utf-8'
ini_path = '/home/carlo/pyramid/carlo/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')


#from pyramid.paster import get_app, setup_logging
#ini_path = '/home/carlo/production.ini'
#setup_logging(ini_path)
#application = get_app(ini_path, 'main')


