pal = 0
palavra = input()
txt = palavra[::-1]
if palavra.count('a') == len(palavra):
    pal = 0
elif txt == palavra:
    pal = len(palavra) - 1
else:
    pal = len(palavra)
print(pal)
