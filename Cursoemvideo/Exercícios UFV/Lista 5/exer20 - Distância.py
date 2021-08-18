dist = 0
a = 0
b = 0

while True:
    if a + b == 2000 and dist != 0:
        break

    a += 10
    b += 15
    dist += 1

print("Distância A: " + str(a) +
      "\nDistância B: " + str(b))