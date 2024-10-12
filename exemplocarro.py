class Carro:

    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro(nome = 'Celta')
celta.acelerar()

armando = Carro("armando")
armando.acelerar()
