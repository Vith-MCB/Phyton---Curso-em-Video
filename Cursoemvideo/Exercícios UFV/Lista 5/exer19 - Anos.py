anos = 0
a = 5000000
b = 7000000
while a <= b:
    a *= 1.02
    b *= 1.02
    anos += 1
print("Demorará " + str(anos) + " anos.")