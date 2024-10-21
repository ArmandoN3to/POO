class Aluno:
    def __init__(self,nome,matricula):
        self.__nome = nome
        self.__matricula=matricula

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula

    def mostrar_info(self):
        return print(f'Nome: {self.nome} Matricula: {self.matricula}')
    

class Curso:
    alunos=[]
    def __init__(self,nome,codigo):
        self.__nome = nome
        self.__codigo = codigo
        self.__alunos = Curso.alunos

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    
    def add_alunos(self,aluno):
        self.alunos.append(aluno)
        print("Aluno adicionado com sucesso...\n")

    def mostrar_alunos(self):
        return print(Curso.alunos)
    
    def devolve_curso(self):
        return {self.nome, self.codigo}
    
class Escola:
    cursos=[]

    def __init__(self,nome):
        self.__nome =nome
        self.__cursos = Escola.cursos

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def add_cursos(self,curso):
        self.cursos.append(curso)
        print("Curso adicionado com sucesso...\n")

    def mostrar_cursos(self):
        for curso in self.cursos:
            print(curso)


a1= Aluno("armando",'123')
curso = Curso("engenharia","456")
escola = Escola("Doroteia")

a1.mostrar_info()
curso.add_alunos(a1)
curso.mostrar_alunos()
escola.add_cursos(curso.devolve_curso())
escola.mostrar_cursos()

