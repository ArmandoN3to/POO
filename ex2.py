class Produto:
    def __init__(self,nome,preco,quantidade):
        self.__nome= nome                                 #criar getters e setters
        self.__preco =preco
        self.__quantidade=quantidade
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,novo_preco):
        self.__preco = novo_preco

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self,novo_quantidade):
        self.__quantidade = novo_quantidade
        

    def ver_quantidade(self):
        print(self.quantidade)
