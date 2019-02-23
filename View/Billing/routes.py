from View.Billing.billing_views import charge_account


def init_billing_routes(app):
    if app:
        app.add_url_rule('/billing/charge_account', 'charge_account', charge_account, methods=['POST'])
