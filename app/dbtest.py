from flask import Flask, jsonify, request
import _mssql

from app.decorators import token_required

app = Flask(__name__)
app.config['DEBUG'] = True


def my_msg_handler(msgstate, severity, srvname, procname, line, msgtext):
    return msgtext


def mssqltest():

    arr_result = list()
    conn = _mssql.connect(server='(local)', user='SA', password='123qaz#@!', database='test')

    try:
        conn.set_msghandler(my_msg_handler)
        conn.execute_query('select getdate()')
    except _mssql.MssqlDatabaseException as e:
        if e.severity == 16:
            # do something
            arr_result.append('DB Error')
        else:
            raise

    for row in conn:
        arr_result.append(row)

    conn.close()

    return jsonify(arr_result)

