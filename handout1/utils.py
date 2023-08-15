def extract_route(request: str):
    return request.split()[1][1:]

def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    return content
