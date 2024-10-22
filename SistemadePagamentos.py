class Funcionario:
    def __init__(self, nome, id_funcionario, salario_base):
        self._nome = nome
        self._id_funcionario = id_funcionario
        self._salario_base = salario_base

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def id_funcionario(self):
        return self._id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, value):
        self._id_funcionario = value

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, value):
        self._salario_base = value

    def calcular_pagamento(self):
        pass
    def adicionar_bonus(self) :   
        pass
    def mostrar_info(self)->None:
        print(f"Nome: {self.nome} ID: {self.id_funcionario},Salario Base: {self.salario_base}")

class FuncionarioClt(Funcionario):

    def __init__(self, nome, id_funcionario, salario_base):
        super().__init__(nome, id_funcionario, salario_base)

    def calcular_pagamento(self):
        total_bonus = self.adicionar_bonus
        self.salario_base+=sum(total_bonus)

    def adicionar_bonus(self,bonus=None):
        bonus_recebido=[]
        bonus_recebido.append(bonus)
        return bonus_recebido
        
class FuncionarioHorista(Funcionario):
    
    def __init__(self, nome, id_funcionario ,horas_trabalhadas,valor_hora:float):
        self.horas_trabalhadas =  horas_trabalhadas
        self.valor_hora = valor_hora
        super().__init__(nome, id_funcionario)

    def calcular_pagamento(self):
        salario = self.horas_trabalhadas*self.valor_hora
    




    
