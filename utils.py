import json
from database import *

def extract_route(request: str):
    return request.split()[1][1:]

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()
    
# def load_data(name: str):
#     with open(('data/' + name), 'r', encoding='utf-8') as file:
#         return json.load(file)
    
def load_data(database: Database):
    return database.get_all()

def load_template(filename: str):
    with open(("templates/" + filename), "r", encoding="utf-8") as file:
        return str(file.read())

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '' and body == '':
        response = 'HTTP/1.1 {code} {reason}\n\n'
    elif body == '':
        response = 'HTTP/1.1 {code} {reason}\n{headers}\n\n'
    elif headers == '':
        response = 'HTTP/1.1 {code} {reason}\n\n{body}'
    else:
        response = 'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    
    return response.format(body=body, code=code, reason=reason, headers=headers).encode()

