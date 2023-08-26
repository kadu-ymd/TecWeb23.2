from utils import load_data, load_template, build_response
from urllib import parse
from database import *

def index(request):
    # Carregando a base de dados
    db = Database('teste')

    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        print(partes)

        # o request não possui um corpo, então não dá para adicionar um item à lista
        
        # for item in corpo.split('&'):
            # print(item)
            # key = item.split('=')[0]
            # params[key] = parse.unquote_plus(item.split('=')[1])
        
        # Adiciona uma nota à base de dados
        # db.add(Note(title=params['titulo'], content=params['detalhes']))

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in load_data(db)
    ]

    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))