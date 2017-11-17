from werkzeug.contrib.profiler import ProfilerMiddleware

from app import create_app

application = create_app('config.DevConfig')

if application.config.get('PROFILE', False):
    restrictions = application.config.get('PROFILE_RESTRICTIONS') or []
    application.wsgi_app = ProfilerMiddleware(application.wsgi_app, restrictions=restrictions)
