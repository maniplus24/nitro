from flask import jsonify, request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

from View.User.schemas import edit_profile_schema, schema
from app.dbconnect import query_mssql
from app.decorators import token_required


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


# edit profile service
class EditProfileInputs(Inputs):  # create a class extending the Inputs class of Flask-Inputs
    json = [JsonSchema(schema=edit_profile_schema)]  # feed your schema here


@token_required
def edit_profile():

    inputs = EditProfileInputs(request)

    if not inputs.validate():
        return jsonify(success=False, errors=inputs.errors)
    else:

        query = 'select getdate();'
        result = query_mssql(query)  # this function gets a query, executes in mssql and returns the result
        return jsonify(result)

