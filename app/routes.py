from View.User.user_views import hello_world
from app.dbtest import mssqltest


def init_api_routes(app):
    if app:
        app.add_url_rule('/', 'hello_world', hello_world, methods=['POST'])
        app.add_url_rule('/mssqltest', 'mssqltest', mssqltest, methods=['POST', 'GET'])
