
ls = [8,3,11,15]
n = int(input())

lstotal = []

for c in range(len(ls) - 1):
    if ls[c] +ls[c + 1 ] == n:
        lstotal.append(c)
        lstotal.append(c + 1)
print(lstotal)
