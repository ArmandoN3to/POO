class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def informacao_genericas(self):
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo,numero_portas:int):
        self.numero_portas = numero_portas
        super().__init__(marca, modelo)
    
    def informacao_genericas(self):
        return super().informacao_genericas()
    
    def informacao_especificas(self):
        print(f'Numero de Portas: {self.numero_portas}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, numero_rodas):
        self.numero_rodas=numero_rodas
        super().__init__(marca, modelo)

    def informacao_genericas(self):
        return super().informacao_genericas()
    
    def informacao_especificas(self):
        print(f'Numero de rodas : {self.numero_rodas}')

class Caminhao(Veiculo):

    def __init__(self, marca, modelo,carga):
        self.carga = carga
        super().__init__(marca, modelo)

    def informacao_genericas(self):
        return super().informacao_genericas()

    def informacao_especificas(self):
        print (f'Peso da carga: {self.carga}')

moto=Moto('ford','ultra' , 2)
carro =Carro('fiat', 'toro', 4)
caminhao =Caminhao('mercedes','benz', 500)

print("CARRO")
carro.informacao_genericas()
carro.informacao_especificas()

print()

print("MOTO")
moto.informacao_genericas()
moto.informacao_especificas()

print()

print("CAMINHAO")
caminhao.informacao_genericas()
caminhao.informacao_especificas()



    
        