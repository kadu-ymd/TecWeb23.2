from database import *

db = Database('notes')

note_list = db.get_all()

# db.add(Note(title="Receita de miojo", content="Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)"))
# db.add(Note(title="Pão doce", content="Abra o pão e coloque o seu suco em pó favorito."))
# db.add(Note(title="Sorvete com cristais de leite", content="Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima."))
# db.add(Note(title="Iogurte natural", content="Deixe o leite fora da geladeira (esse é mentira, não faça isso)."))
# db.add(Note(title="Homer Simpson", content="~( 8(|)"))
# db.add(Note(title="Série da Fundação - Isaac Asimov", content="É boa, leia."))

for dados in note_list:
    print(dados)