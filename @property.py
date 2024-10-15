class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property  #é uma propriedade do objeto e, é um metodo que se comporta com atributo   
    def cor(self):
        print("Property")
        return self.cor_tinta #fez um metodo se comportar como uma instancia
    
    # @cor.setter
    # def cor(self):

    def get_cor(self):              #getter Padrao
        print("Getter padrao")
        return self.cor_tinta
    
caneta = Caneta('Azul')
print(caneta.cor)       #aqui é property
print(caneta.cor)
print(caneta.cor)

print(caneta.get_cor())
print(caneta.get_cor())     #aqui é o getter padrao
print(caneta.get_cor())
