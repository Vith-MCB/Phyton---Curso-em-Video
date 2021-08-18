saldo = float(input())
if saldo in range(0, 501):
    print('Nenhum credito')
elif saldo in range(501, 1001):
    cred = saldo
    cred *= 0.3
    print('Saldo: {} | Credito: {:.2f}'.format(saldo, cred))
elif saldo in range(1001, 3001):
    cred = saldo
    cred *= 0.4
    print('Saldo: {} | Credito: {:.2f}'.format(saldo, cred))
elif saldo > 3001:
    cred = saldo
    cred *= 0.5
    print('Saldo: {} | Credito: {:.2f}'.format(saldo, cred))
