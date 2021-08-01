n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    if n1 > n3 and n3 > n2:
       print('Maior: {} // Menor: {}'.format(n1, n2))
    else:
        print('Maior: {} // Menor: {}'.format(n3, n2))
if n2 > n1:
    if n2 > n3 and n3 > n1:
       print('Maior: {} // Menor: {}'.format(n2, n1))
    else:
        print('Maior: {} // Menor: {}'.format(n3, n1))