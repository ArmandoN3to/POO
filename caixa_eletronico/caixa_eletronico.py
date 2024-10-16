from movimentacao import Movimentacao

try:
    p1 = Movimentacao('Armando','06044526240',400.00,'1234')
    while True:
        print('='*40)
        print(' '*10,'Caixa Eletronico')
        print('1 - Saque')
        print('2 - Deposito')
        print('3 - Fazer transferencia')
        print('4 - Mostrar Saldo')
        print('5 - Mostrar informaçoes da conta')
        print('6 - Sair')
        print('='*40)
    
        opcao = int(input('Digite sua opcao: '))

        if opcao == 6:
            break
        else:
            p1.operacao(opcao)

except Exception as e:
    print(e)
finally:
    print()
    print("Operaçao Finalizada")
