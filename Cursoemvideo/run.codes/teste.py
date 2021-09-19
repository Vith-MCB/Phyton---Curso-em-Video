alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z']
palavra = input()
cont = 0
txt = palavra[::-1]
for j in range(26):
    letra = alf[j]
    cont = palavra.count(letra)
