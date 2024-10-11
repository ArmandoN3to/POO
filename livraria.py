class Biblioteca:

    def __init__(self,livro):
        self.livro = livro

    def adicionar_livros(self):
        pass
    def emprestar_livros(self):
        pass
    def verificar_inventario(self):
        pass

class Livro:
        def __init__(self,titulo,autor,disponivel):
            self.titulo = titulo
            self.autor = autor
            self.disponivel = True
            
        def emprestar(self):
            self.disponivel = False

        def devolver(self):
            self.disponivel = True
        def mostrar_info(self,):
            pass