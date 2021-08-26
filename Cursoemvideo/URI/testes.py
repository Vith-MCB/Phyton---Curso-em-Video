X = []
for y in range(10):
    X.append(int(input()))
    if X[y] <= 0:
        X[y] = 1
for i in range(len(X)):
    print(f'X[{i}] =', X[i])
