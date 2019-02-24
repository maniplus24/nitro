from flask import jsonify, Blueprint

from View.User.schemas import edit_profile_schema, schema
from app.dbconnect import query_mssql
from app.decorators import token_required, validate_schema

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/', methods=['POST'])
@validate_schema(schema)
@token_required
def hello_world():

    query = 'select getdate();'
    return jsonify(query_mssql(query))


@user_blueprint.route('/user/edit_profile', methods=['POST'])
@validate_schema(edit_profile_schema)
@token_required
def edit_profile():

    query = 'select getdate();'
    result = query_mssql(query)  # this function gets a query, executes in mssql and returns the result
    return jsonify(result)

