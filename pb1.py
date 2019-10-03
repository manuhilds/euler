""" Natural numbers """

i = 1000
j = []
for n in range(1, i):
    if n % 3 == 0 or n % 5 == 0:
        j.append(n)

print(j)
print(sum(j))
