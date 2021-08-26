import math
num = [int(input()) for i in range(5)]
for i in range(5):
    if num[i] < 0:
        num[i] = -1
    else:
        num[i] = math.sqrt(num[i])
print(num)
