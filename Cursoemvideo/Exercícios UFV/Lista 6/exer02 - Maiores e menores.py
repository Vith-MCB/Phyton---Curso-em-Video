n = []
num = int(input())
for i in range(10):
    n.append(int(input()))
for i in range(10):
    if n[i] < num:
        print(n[i])
