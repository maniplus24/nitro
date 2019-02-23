schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string', 'minLength': 3}
    },
    'required': ['name', ]
}


# for each service write a schema and import it in the service views file
edit_profile_schema = {
    'type': 'object',
    'properties': {
        'nickname': {'type': 'string', 'minLength': 3}
    },
    'required': ['nickname', ]
}
