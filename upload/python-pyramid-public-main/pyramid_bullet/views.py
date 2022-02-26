from pyramid.view import view_config

import os

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'pyramid_bullet', 'env': os.environ.get('FOO')}
