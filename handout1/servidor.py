import socket
from pathlib import Path
from utils import extract_route, read_file, load_data

CUR_DIR = Path(__file__).parent
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

NOTE_TEMPLATE = '''  <li>
    <h3>{title}</h3>
    <p>{details}</p>
  </li>
'''

RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="handout1/img/logo-getit.png">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{notes}
</ul>

<ul>
  <li>
    <h3>Receita de miojo</h3>
    <p>Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)</p>
  </li>
  <li>
    <h3>Pão doce</h3>
    <p>Abra o pão e coloque o seu suco em pó favorito.</p>
  </li>
  <li>
    <h3>Sorvete com cristais de leite</h3>
    <p>Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima.</p>
  </li>
  <li>
    <h3>Iogurte natural</h3>
    <p>Deixe o leite fora da geladeira (esse é mentira, não faça isso).</p>
  </li>
  <li>
    <h3>Homer Simpson</h3>
    <p>~( 8(|)</p>
  </li>
  <li>
    <h3>Numero mágico</h3>
    <p>142857</p>
  </li>
  <li>
    <h3>Série da Fundação - Isaac Asimov</h3>
    <p>É boa, leia.</p>
  </li>
</ul>

</body>
</html>
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        response = 'HTTP/1.1 200 OK\n\n'.encode() + read_file(filepath)
    else:
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        notes_li = [
            NOTE_TEMPLATE.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)

        response = RESPONSE_TEMPLATE.format(notes=notes).encode()
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()