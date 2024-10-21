class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    @property        
    def titulo(self):                       #tem que vir antes dos metodos os getters e os setters
        return self.__titulo
    
    @titulo.setter
    def titulo(self,novo_titulo):
        self.__titulo = novo_titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,novo_autor):
        self.__autor = novo_autor
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self,novo_disponivel):
        self.__disponivel= novo_disponivel    

    def emprestar(self):
        if self.disponivel:         #CHECAR SE AS VARIAVEIS ESTAO NO TIPO PROPERTY
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já estava disponível.")

    def mostrar_disponibilidade(self):
        status = "disponível" if self.disponivel else "emprestado"
        print(f"'{self.titulo}' de {self.autor} está {status}.")


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)
        print(f"Livro '{titulo}' de {autor} foi adicionado ao acervo.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f"Livro '{titulo}' não encontrado no acervo.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.devolver()
                return
        print(f"Livro '{titulo}' não encontrado no acervo.")

    def mostrar_inventario(self):
        print("\nInventário da Biblioteca:")
        for livro in self.livros:
            livro.mostrar_disponibilidade()
        print("-" * 40)

biblioteca = Biblioteca()

biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes")
biblioteca.adicionar_livro("1984", "George Orwell")
biblioteca.adicionar_livro("A Revolução dos Bichos", "George Orwell")

biblioteca.mostrar_inventario()

biblioteca.emprestar_livro("1984")
biblioteca.emprestar_livro("A Revolução dos Bichos")
biblioteca.mostrar_inventario()

biblioteca.devolver_livro("1984")
biblioteca.mostrar_inventario()