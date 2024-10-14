class Pessoa:
    ano_atual = 2024  #Atributo de CLASSE

    def __init__(self,nome,idade):
        self.nome =nome
        self.idade = idade

    def get_ano_nascimento(self):
        return print(f'O ano de nascimento do(a) {self.nome} = {Pessoa.ano_atual - self.idade}')
    
print(Pessoa.ano_atual)  #chamando atributo de classe

dados ={'nome': 'Armando', 'idade': 21, 'Cabelo': 'Enrolado'}  

p1 = Pessoa('Armando',21)
p1.get_ano_nascimento()   

p2 = Pessoa("Vitoria",24)
p2.get_ano_nascimento()

# p1.__dict__['nome'] = 'Carlos'
# p1.__dict__['Cabelo'] = 'Enrolado'
# p2.__dict__['Cabelo'] = 'Liso'

print(p1.__dict__)
print(dados['Cabelo'])