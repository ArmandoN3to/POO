#O aluno deverá criar um sistema de pagamentos que utiliza polimorfismo
# para processar diferentes tipos de pagamentos.

class Pagamento:
    def processar_pagamento(self):
        pass

class PagamentoCartaoCredito(Pagamento):
    def __init__(self,numero_cartao=None):
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        return print(f"o Pagamento no cartao de credito {self.numero_cartao} foi processado")
    
class PagamentoBoleto(Pagamento):
    def __init__(self,cod=None) :
        self.cod=cod
    def processar_pagamento(self):
        return print(f"pagamento do boleto {self.cod} foi processado")

class PagamentoPix(Pagamento):

    def __init__(self,chave_pix=None):
        self.chave_pix=chave_pix

    def processar_pagamento(self):
        return print(f"o pagamento pix foi processado {self.chave_pix}")
    
def processsar(obj):
    if isinstance(obj,PagamentoCartaoCredito):
        PagamentoCartaoCredito.processar_pagamento(obj)
    if isinstance(obj,PagamentoBoleto):
        PagamentoBoleto.processar_pagamento(obj)
    if isinstance(obj,PagamentoPix):
        PagamentoPix.processar_pagamento(obj)

cartao = PagamentoCartaoCredito("a231231")
boleto = PagamentoBoleto("2837183ndsd")
pix = PagamentoPix("97492141")

print()
processsar(cartao)
print()
processsar(boleto)
print()
processsar(pix)
    