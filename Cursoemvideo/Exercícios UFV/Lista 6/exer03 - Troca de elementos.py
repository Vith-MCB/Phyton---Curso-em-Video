vet = [int(input()) for i in range(20)]
for i in range(len(vet)//2):
    guarda = vet[len(vet) - i - 1]
    vet[len(vet) - i - 1] = vet[i]
    vet[i] = guarda
print(vet)
