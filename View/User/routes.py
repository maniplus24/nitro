from View.User.user_views import hello_world, edit_profile


def init_user_routes(app):
    if app:
        app.add_url_rule('/user/', 'hello_world', hello_world, methods=['POST'])
        app.add_url_rule('/user/edit_profile', 'edit_profile', edit_profile, methods=['POST'])  # for each service write a route first
