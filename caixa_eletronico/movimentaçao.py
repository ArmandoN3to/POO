from cliente import Cliente
from conta import Conta

class Movimentacao:
    id= 0
    def __init__(self,nome,cpf,saldo,numero,data_atual=None,hora=None):
        # self.data_atual=data_atual
        # self.hora = hora
        self.cliente = Cliente(cpf,nome)
        self.conta = Conta(numero,saldo)

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id_novo):
        self.__id = id_novo

    def operacao(self,tipo_operacao):
        match tipo_operacao :
            case 1 : 
                valor = float(input("Digite o valor do saque: "))
                self.conta.sacar(valor)
            case 2 :
                valor= float(input("Digite o valor do deposito: "))
                self.conta.depositar(valor)
            case 3:
                valor = float(input("Digite o valor da tranferencia: "))
                self.conta.transferir(valor)



        


        