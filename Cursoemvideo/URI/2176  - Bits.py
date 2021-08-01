s = input()
lens = len(s)
contador1 = 0
while lens != 0:
    lens -= 1
    if s[lens] == '1':
        contador1 += 1
if contador1 % 2 == 0:
    s += '0'
else:
    s += '1'
print(s)
