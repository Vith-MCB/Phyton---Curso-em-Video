'''
N = int(input())
notas100 = N//100
notas50 = (N-(notas100*100))//50
notas20 = (N-(notas100*100+notas50*50))//20
notas10 = (N-(notas100*100+notas50*50+notas20*20))//10
notas5 = (N-(notas100*100+notas50*50+notas20*20+notas10*10))//5
notas2 = (N-(notas100*100+notas50*50+notas20*20+notas10*10+notas5*5))//2
notas1 = (N-(notas100*100+notas50*50+notas20*20+notas10*10+notas5*5+notas2*2))

print(notas100, ' nota(s) de R$ 100,00')
print(notas50, ' nota(s) de R$ 50,00')
print(notas20, ' nota(s) de R$ 20,00')
print(notas10, ' nota(s) de R$ 10,00')
print(notas5, ' nota(s) de R$ 5,00')
print(notas2, ' nota(s) de R$ 2,00')
print(notas1, ' nota(s) de R$ 1,00')
'''
N = int(input())
n100 = N//100
N = N - n100*100
n50 = N//50
N = N - n50*50
n20 = N//20
N = N - n20*20
n10 = N//10
N = N - n10*10
n5 = N//5
N = N - n5*5
n2 = N//2
N = N - n2*2
n1 = N
print(n100, ' nota(s) de R$ 100,00')
print(n50, ' nota(s) de R$ 50,00')
print(n20, ' nota(s) de R$ 20,00')
print(n10, ' nota(s) de R$ 10,00')
print(n5, ' nota(s) de R$ 5,00')
print(n2, ' nota(s) de R$ 2,00')
print(n1, ' nota(s) de R$ 1,00')