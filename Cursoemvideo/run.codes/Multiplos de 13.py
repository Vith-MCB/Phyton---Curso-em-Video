x = int(input())
y = int(input())
soma13 = 0
if x > y:
    for i in range(y, x+1):
        if i % 13 != 0:
            soma13 += i
if x < y:
    for i in range(x, y+1):
        if i % 13 != 0:
            soma13 += i
print(soma13)
