Guarda = 0
Guarda_m = float('inf')
for i in range(0, 1000):
    x = int(input())
    if x > Guarda:
        Guarda = x
    elif x < Guarda_m:
        Guarda_m = x
print(Guarda_m)
print(Guarda)