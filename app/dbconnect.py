import _mssql


def my_msg_handler(msgstate, severity, srvname, procname, line, msgtext):
    return msgtext


def query_mssql(query):

    conn = _mssql.connect(server='(local)', user='SA', password='123qaz#@!', database='test')

    try:
        conn.set_msghandler(my_msg_handler)
        conn.execute_query(query)
    except _mssql.MssqlDatabaseException as e:
        if e.severity == 16:
            # do something
            pass
        else:
            raise

    result = [row for row in conn]

    conn.close()

    return result
