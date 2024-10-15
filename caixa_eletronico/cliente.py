class Cliente:
    def __init__(self,cpf=str,nome=str):
        self.__cpf=cpf
        self.__nome =nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,novo_cpf):
        if self.__cpf!= None:
            self.__cpf=novo_cpf
        else:
            print("Nao foi possivel settar o valor")

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novo_nome):
        if self.__nome!=None:
            self.__nome=novo_nome
    
    def info_cliente(self):
        pass
        