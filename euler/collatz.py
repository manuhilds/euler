tmp =[1,0]
for n in range(10,1000000):
	i=0
	m=n
	while n!=1:
		if(n%2==0):
			n/=2
		else:
			n=3*n+1
		i+=1
	if tmp[0]<i:
		tmp[0]=i
		tmp[1]=m
print tmp[1]
