from pyramid.config import Configurator



def main(global_config, **settings):

    config = Configurator(settings=settings)
    config.include("pyramid_jinja2")
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.add_route('home', '/')


    config.add_route('hello_json', '/howdy.json')

    config.scan('.views')
    config.add_jinja2_renderer(".html")
    config.add_jinja2_renderer(".xhtml")
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
