from pyramid.renderers import JSON
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('menu', '/menu', )
    config.add_route('upload_form', '/upload', )
    config.add_route('store_mp3_view', '/store_mp3_view', )
    config.add_route('slide', '/slide', )
    config.add_route('newss', '/newss', )
    config.add_route('news_one', '/news_one', )
    config.add_route('sanpiero', '/sanpiero')
    config.add_route('mugello', '/mugello')