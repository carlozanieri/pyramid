from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError
from carlo.Connect import Connect
from .. import models
import os
import shutil

from pyramid.response import Response

@view_config(route_name='store_mp3_view', renderer='carlo:templates/upload_form.jinja2')
def store_mp3_view(request):
    # ``filename`` contains the name of the file in string format.
    #
    # WARNING: Internet Explorer is known to send an absolute file
    # *path* as the filename.  This example is naive; it trusts
    # user input.
    filename = request.POST['file'].filename
    dirname = request.POST['dir']

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.
    input_file = request.POST['file'].file

    # Using the filename like this without cleaning it is very
    # insecure so please keep that in mind when writing your own
    # file handling.
    file_path = os.path.join(dirname, filename)
    with open(file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    return Response(' File  ' + filename + '  salvato correttamente' )

@view_config(route_name='home', renderer='carlo:templates/mytemplate.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'carlo', "menu":Connect.menu(""), "submenu":Connect.submnu(""),"pagina":Connect.body("", "index"),  "luogo" : "index"}
db_err_msg = """\


Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

@view_config(route_name='menu', renderer='carlo:templates/menu.jinja2')
def menu(request):
    return {"greet": 'Welcome', "name": 'Akhenaten',"menu":Connect.menu(""), "submenu":Connect.submnu(""),"pagina":Connect.body("", "index"), "renderer":'json'}

@view_config(route_name='upload_form', renderer='carlo:templates/upload_form.jinja2')
def menu(request):
    return {"greet": 'Welcome', "name": 'Akhenaten',"menu":Connect.menu(""), "submenu":Connect.submnu(""), "pagina":Connect.body("", "index"), "renderer":"json"}

@view_config(route_name='slide', renderer='carlo:templates/nivo.jinja2')
def slide(request):
    #luogo = request.POST['luogo']
    luogo = request.params['luogo']

    return {"luogo":luogo, "slider":Connect.slider("", luogo), "renderer": "json"}


@view_config(route_name='newss', renderer='carlo:templates/news.jinja2')
def newss(request):
    return { "pagina":Connect.body("", "sanpiero"), "manifestazione":"news", "news":Connect.news("")}

@view_config(route_name='news_one', renderer='carlo:templates/news_one.jinja2')
def news_one(request):
    titolo=request.POST['titolo']
    id=request.POST['id']
    return { "pagina":Connect.body("", "sanpiero"), "manifestazione":"news", "news":Connect.news_one("",titolo, id)}

@view_config(route_name='sanpiero', renderer='carlo:templates/mytemplate.jinja2')
def sanpiero(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'carlo', "menu":Connect.menu(""), "submenu":Connect.submnu(""),"pagina":Connect.body("", "sanpiero"), "luogo" : "sanpiero"}

@view_config(route_name='mugello', renderer='carlo:templates/mytemplate.jinja2')
def mugello(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'carlo', "menu":Connect.menu(""), "submenu":Connect.submnu(""),"pagina":Connect.body("", "mugello"), "luogo" : "mugello"}
