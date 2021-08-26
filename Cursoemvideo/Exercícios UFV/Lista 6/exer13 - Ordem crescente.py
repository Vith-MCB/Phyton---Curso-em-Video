vet = [int(input()) for i in range(5)]
guarda = 0
for i in range(5):
    if vet[i] > vet[i+1]:
        guarda = vet[i]
        vet[i] = vet[i+1]
        vet[i+1] = guarda
print(vet)
