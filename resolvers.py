def resolve_hello(obj, info):
    return "Hello, world!"

def resolve_greeting(obj, info, name):
    return f"Hello, {name}!"

people_db = {
    "1": {"id": "1", "name": "Fabian", "age": 50},
    "2": {"id": "2", "name": "Ricardo", "age": 70},
}

def resolve_getPerson(obj, info, id):
    return people_db.get(id)
