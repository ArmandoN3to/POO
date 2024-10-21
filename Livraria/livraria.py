class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, value):
        self.__nacionalidade = value


    def mostrar_info(self):
        return f"Autor: {self.nome}, Nacionalidade: {self.nacionalidade}"


class Livro:
    def __init__(self, titulo, isbn, ano_publicacao):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__ano_publicacao = ano_publicacao
        self.__autores = []

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def ano_publicacao(self):
        return self.__ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, value):
        self.__ano_publicacao = value

    @property
    def autores(self):
        return  self.__autores
    
    @autores.setter
    def autores(self,value):
        self.__autores=value

    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def mostrar_info(self):
        autores_info = ', '.join([autor.nome for autor in self.autores])
        return f"Título: {self.titulo}, ISBN: {self.isbn}, Ano de Publicação: {self.ano_publicacao}, Autores: {autores_info}"


class Leitor:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.historico_emprestimos=[]

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        self.__idade = value

        self.historico_emprestimos = []

    def mostrar_info(self):
        return f"Leitor: {self.nome}, Idade: {self.idade}"

    def adicionar_emprestimo(self, emprestimo):
        self.historico_emprestimos.append(emprestimo)


class Emprestimo:
    def __init__(self, leitor, livro, data_emprestimo, data_devolucao=None):
        self.__leitor = leitor
        self.__livro = livro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao

    @property
    def leitor(self):
        return self.__leitor

    @leitor.setter
    def leitor(self, value):
        self.__leitor = value

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, value):
        self.__livro = value

    @property
    def data_emprestimo(self):
        return self.__data_emprestimo

    @data_emprestimo.setter
    def data_emprestimo(self, value):
        self.__data_emprestimo = value

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    @data_devolucao.setter
    def data_devolucao(self, value):
        self.__data_devolucao = value

    def mostrar_info(self):
        devolucao_info = self.data_devolucao if self.data_devolucao else "Não devolvido"
        return (f"Leitor: {self.leitor.nome}, Livro: {self.livro.titulo}, "
                f"Data de Empréstimo: {self.data_emprestimo}, Data de Devolução: {devolucao_info}")


class Biblioteca:
    def __init__(self)->None:
        self.livros = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def realizar_emprestimo(self, livro, leitor, data_emprestimo):
        if livro in self.livros:
            if len(leitor.historico_emprestimos) < 3:
                emprestimo = Emprestimo(leitor, livro, data_emprestimo)
                self.emprestimos.append(emprestimo)
                leitor.adicionar_emprestimo(emprestimo)
                self.livros.remove(livro)
                return True
            else:
                print("O leitor já possui o máximo de 3 livros emprestados.")
        else:
            print("O livro não está disponível para empréstimo.")
        return False

    def devolver_livro(self, emprestimo, data_devolucao):
        emprestimo.data_devolucao = data_devolucao
        self.livros.append(emprestimo.livro)

    def mostrar_emprestimos(self):
        return [emprestimo.mostrar_info() for emprestimo in self.emprestimos]

    def mostrar_livros(self):
        return [livro.mostrar_info() for livro in self.livros]

    def relatorio(self):
        total_emprestados = len(self.emprestimos)
        total_disponiveis = len(self.livros)
        return f"Total de livros emprestados: {total_emprestados}, Total de livros disponíveis: {total_disponiveis}"


autor1 = Autor("George Orwell", "Britânico")
autor2 = Autor("Aldous Huxley", "Britânico")

livro1 = Livro("1984", "123456789", 1949)
livro1.adicionar_autor(autor1)
livro1.adicionar_autor(autor2)

livro2 = Livro("Admirável Mundo Novo", "987654321", 1932)
livro2.adicionar_autor(autor2)

leitor1 = Leitor("João", 25)
leitor2 = Leitor("Maria", 30)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.realizar_emprestimo(livro1, leitor1, "2024-10-21")
biblioteca.realizar_emprestimo(livro2, leitor2, "2024-10-21")
biblioteca.realizar_emprestimo(livro2, leitor2, "2024-10-21")

print(biblioteca.mostrar_emprestimos())
print(biblioteca.mostrar_livros())
print(biblioteca.relatorio())