import json
CAMINHO_ARQ = 'JSON_PESSOA'

class Pessoa:
    ano_atual = 2024
    def __init__(self,nome,idade):
        self.nome =nome
        self.idade = idade

    def get_ano_nascimento(self):
        return print(f'O ano de nascimento do(a) {self.nome} = {Pessoa.ano_atual - self.idade}')
    
p1 = Pessoa('Armando',21)
p2 = Pessoa('Vitoria',24)
p3 = Pessoa('Joao',26)

lista = [vars(p1),p2.__dict__,vars(p3)]

def fazendo_dump():
    with open(CAMINHO_ARQ,'w') as arquivo:
        json.dump(lista,arquivo, ensure_ascii = False,indent = 2)

if __name__ == '__main__':
    print('Esse é o __main__')
    fazendo_dump()


    