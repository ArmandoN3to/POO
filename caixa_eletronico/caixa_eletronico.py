from movimentaçao import Movimentacao

teste = Movimentacao('123''Armando','06044526240',400.00,'1234')
while True:
    print('='*40)
    print(' '*10,'Caixa Eletronico')
    print('1 - Saque')
    print('2 - Deposito')
    print('3 - Fazer transferencia')
    print('4 - Sair')
    operacao = int(input('digite sua opcao: '))
    print('='*40)
    if operacao == 4:
        break
    else:
        teste.operacao(operacao)
