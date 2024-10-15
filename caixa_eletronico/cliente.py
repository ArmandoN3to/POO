class Cliente:
    def __init__(self,cpf,nome):
        self.__cpf=cpf
        self.__nome =nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,novo_cpf):
        self.__cpf=novo_cpf

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,novo_nome):
        self.__nome=novo_nome


    
        