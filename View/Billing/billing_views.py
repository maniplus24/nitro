from flask import jsonify, request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from View.Billing.schemas import charge_account_schema
from app.dbconnect import query_mssql
from app.decorators import token_required


class ChargeAccountInputs(Inputs):
    json = [JsonSchema(schema=charge_account_schema)]


@token_required
def charge_account():
    inputs = ChargeAccountInputs(request)

    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)
    else:

        query = 'select getdate();'
        return jsonify(query_mssql(query))
