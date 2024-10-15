from datetime import datetime

class Conta:
    data_hora_atual = datetime.now()
    data_formatada = data_hora_atual.strftime('%d/%m/%Y')
    hora_formatada = data_hora_atual.strftime('%H:%M:%S')
    def __init__(self,numero:int,saldo:float):
        self.__numero = numero
        self.__saldo=saldo

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,novo_numero):
        self.__numero=novo_numero
        
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo=novo_saldo

    def sacar(self,quantidade:float):
        if self.saldo == 0:
            print(f'voce nao tem dinheiro para sacar / SEU SALDO: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
        elif quantidade <0:
            print(f'Voce nao pode sacar um numero negativo / SALDO: {self.saldo}/ DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
        elif self.saldo<quantidade:
            print(f'Voce nao tem essa quantidade para realizar o saque / SEU SALDO: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
        else:
            self.saldo=self.saldo - quantidade
            print(f'Saque realizado com sucesso / QUANTIDADE DE SAQUE {quantidade} / SEU SALDO: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
            
    def depositar(self,deposito:float):
        if deposito<0:
            print(f"Voce nao pode fazer um deposito de um numero negativo / SEU SALDO: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}")
        else:
            self.saldo=self.saldo+deposito
            print(f'Voce fez o deposito de {deposito} / SEU SALDO: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
    def transferir(self,transferencia:float,):
        if transferencia<0:
            print(f'Voce nao pode fazer uma tranferencia negativa / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
        else:
            conta_transferencia= input("Digite o numero da conta que voce deseja fazer a transferencia: ")
            print(f'Voce fez uma transferencia de {transferencia} para a conta: {conta_transferencia} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
            
    def mostrar_informacoes(self):
        print(f"ID: {self.id}")
        print(f"Numero: {self.numero}")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Saldo: {self.saldo}")

    def mostrar_saldo(self):
        print(f'O seu SALDO É DE: {self.saldo} / DATA : {Conta.data_formatada} HORA: {Conta.hora_formatada}')
