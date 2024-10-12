class Camera:
    def __init__(self,nome,filmando = False):
        self.nome =nome
        self.filmando = filmando
    def filmar(self):
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_de_filmar(self):
        print(f'{self.nome} está parando de filmar')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando is True:
            print(f'{self.nome} NAO pode fotografar pois ja esta filmando..')
            return
        print(f'{self.nome} está fotografando')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.parar_de_filmar()
c1.fotografar()

print()

c2.filmar()
c2.fotografar()
c2.parar_de_filmar()
c2.fotografar()


