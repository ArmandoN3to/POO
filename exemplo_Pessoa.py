# from calculadoraIMC import Imc

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        self.idade+=anos
    
    def engordar(self,kg):
        self.peso+=kg

    def emagrecer(self,kg):
        self.peso-=kg

    def crescer(self ,cm):
        self.altura+=cm

    def imprimir_dados(self):
        print('='*40)
        print(f'Nome:{self.nome}')
        print(f'idade:{self.idade}')
        print(f'peso:{self.peso}')
        print(f'altura:{self.altura}')
        

p1=Pessoa('Armando',20,70,167)
p1.imprimir_dados()
p1.crescer(10)
p1.emagrecer(5)
p1.engordar(10)
p1.envelhecer(4)
p1.imprimir_dados()

p2=Pessoa('Vitoria',24,56,160)
p2.imprimir_dados()
p2.crescer(5)
p2.emagrecer(0)
p2.envelhecer(3)
p2.imprimir_dados()