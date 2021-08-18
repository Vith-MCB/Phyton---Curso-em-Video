fibonacci = [0, 1]
n = int(input())
if n == 1:
    print(str(fibonacci[0]))

if n < 46 and n > 1:
    if n > 2:
        for x in range(n - 2):
            fibonacci.append(fibonacci[x] + fibonacci[x + 1])

    myTable = str(fibonacci).maketrans("", "", "[,]")

    print(str(fibonacci).translate(myTable))
