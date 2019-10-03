oui = tuple((0, 0))
n = 1000
h = []
for i in range(1, n):
    for a in range(1, i):
        if str(i*a) == str(i*a)[::-1]:
            h.append(tuple((i, a)))
            if sum(h[-1]) > sum(oui):
                oui = h[-1]

print(h)
print(oui)
print(oui[0]*oui[1])
