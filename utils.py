import json

def extract_route(request: str):
    return request.split()[1][1:]

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()
    
def load_data(filename: str):
    with open(('data/' + filename), 'r') as file:
        return json.load(file)
    
def load_template(filename: str):
    with open(("templates/" + filename),"r") as file:
        return str(file.read())