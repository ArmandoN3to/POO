class Imc:
    def __init__(self,nome,peso,altura,):
        self.peso=peso
        self.altura=altura/100 
        self.nome=nome 

    def calcularimc(self):
        imc=self.peso/(self.altura*self.altura)
        return imc
    
    def mostraratributos(self):
        estado=self.checagem()
        print(f'Nome:{self.nome}')
        print(f'peso:{self.peso}')
        print(f'altura :{self.altura}')
        print(f'estado :{self.estado}')

    def checagem(self):
        imc=self.calcularimc()
        if imc<18.5:
            return "Abaixo do peso"
        elif imc>= 18.5 and imc <= 24.9:
            return "Peso normal"
        elif imc>= 25 and imc <= 29.9:
            return "Sobrepeso"
        elif imc>=30:
            return "Obesidade"
            
nome=str("Digite seu nome: ")
peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura:'))
pessoa1=Imc(nome,peso,altura)
pessoa1.calcularimc()
pessoa1.checagem()
pessoa1.mostraratributos()


