class Calculadora:
    def adicionar(self,*args):
        return(sum(args))
    
calc=Calculadora()
print(calc.adicionar(5))
print(calc.adicionar(5,10))
print(calc.adicionar(5,10,15))
print(calc.adicionar(5,10,15,20))
print(calc.adicionar(5,10,15,20,25))
print(calc.adicionar(5,10,15,20,25,30))
print(calc.adicionar(5,10,15,20,25,30,35,63,89,23,329,3232,323,3232,32,32,313,1,31,323,32,32,32,3,23,23,2323,2,32,32,32323232,32,3,23,23))
