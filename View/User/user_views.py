from flask import jsonify, request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from app.dbconnect import query_mssql
from app.decorators import token_required
from app.schemas import schema


# Sample Service
class HelloWorldInputs(Inputs):
    json = [JsonSchema(schema=schema)]

@token_required
def hello_world():

    inputs = HelloWorldInputs(request)

    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)
    else:

        query = 'select getdate();'
        return jsonify(query_mssql(query))
