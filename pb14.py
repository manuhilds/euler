
n = 1000000

temp = 0
k = 0
for i in range(1,n):
    h = []
    k = i
    while k != 1:
        if k%2 == 0:
            k/=2
        else :
            k*=3
            k+=1
        h.append(i)
    if temp < len(h):
        temp = len(h) 
        j = i
print (j,temp)
    
