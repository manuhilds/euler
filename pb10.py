def soe(n):
    c=0
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        for i in range(p*p, n+1, p):
            prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            c+=p
    print(c)
    return 0
j = 2000000
soe(j)
