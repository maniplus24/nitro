from app.dbtest import mssqltest


def init_api_routes(app):
    if app:
        app.add_url_rule('/mssqltest', 'mssqltest', mssqltest, methods=['POST', 'GET'])
