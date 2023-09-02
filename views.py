from utils import load_data, load_template, build_response
from urllib import parse
from database import *

def index(request):
    # Carregando a base de dados
    db = Database('notes')

    if request.startswith('POST /'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for item in corpo.split('&'):
            key = item.split('=')[0]
            params[key] = parse.unquote_plus(item.split('=')[1])

        # Adiciona, atualiza ou deleta uma nota
        if not request.startswith('POST /delete') and not request.startswith('POST /edit/update'):
            db.add(Note(title=params['titulo'], content=params['detalhes']))
        elif request.startswith('POST /edit/update'):
            db.update(Note(id=int(params['id']), title=params['titulo'], content=params['detalhes']))
        else:
            db.delete(int(params['id']))

        return build_response(code=303, reason='See Other', headers='Location: /')
    
        
    
    if request.startswith('GET /edit'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        header = partes[0].split(' ')
        route = header[1][1:]
        id = int(route.split('/')[1])

        note = db.get_note(id)
        
        return build_response(body=load_template('edit.html').format(id=note.id, title=note.title, details=note.content))
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in load_data(db)
    ]

    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))