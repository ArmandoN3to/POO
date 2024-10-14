class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property  #faz com que o metodo se comporte como uma instancia
    def cor(self):
        print("Property")
        return self.cor_tinta #fez um metodo se comportar como uma instancia
    
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
