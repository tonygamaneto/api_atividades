from models import Pessoas
# insere dados na tabela pessoas
def insere_pessoas():
    pessoa =  Pessoas(nome='Juvenal', idade=23)
    print(pessoa)
    pessoa.save()

#consulta dados na tabela pessoas
def consulta_pessoas():
    pessoa = Pessoas.query.all ()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Juvenal').first()
    print(pessoa, pessoa.idade)

#altera dados na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galeani').first()
    pessoa.nome = 'Roberto'
    pessoa.save()

#exclui dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Roberto').first()
    pessoa.delete()


if __name__ == '__main__':
   #insere_pessoas()
   #altera_pessoa()
   consulta_pessoas()
   #exclui_pessoa()
