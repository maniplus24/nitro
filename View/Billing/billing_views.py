from flask import jsonify, request, Blueprint
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from View.Billing.schemas import charge_account_schema
from app.dbconnect import query_mssql
from app.decorators import token_required, validate_schema

billing_blueprint = Blueprint('billing', __name__)


@billing_blueprint.route('/billing/charge_account', methods=['POST'])
@validate_schema(charge_account_schema)
@token_required
def charge_account():

    query = 'select getdate();'
    return jsonify(query_mssql(query))
