class Conta:

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
            print(f'voce nao tem dinheiro para sacar / SEU SALDO: {self.saldo}')
        elif self.saldo<quantidade:
            print(f'Voce nao tem essa quantidade para realizar o saque / SEU SALDO: {self.saldo}')
        else:
            self.saldo=self.saldo - quantidade
            print(f'Saque realizado com sucesso / QUANTIDADE DE SAQUE {quantidade} / SEU SALDO{self.saldo}')
            
    def depositar(self,deposito:float):
        if deposito<0:
            print(f"Voce nao pode fazer um deposito de um numero negativo / SEU SALDO {self.saldo}")
        else:
            self.saldo=self.saldo+deposito
            print(f'Voce fez o deposito de {deposito} / SEU SALDO: {self.saldo}')
    def transferir(self,transferencia,local:str):
        if transferencia<0:
            print(f'Voce nao pode fazer uma tranferencia negativa')
        else:
            print(f'Voce fez uma transferencia de {transferencia} para {local}')

    def mostrar_saldo(self):
        pass
