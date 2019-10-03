
n = 600851475143

i = 2

while i*i < n:
    while n % i == 0:
        n = n / i
    i = i+1

print(n)
# while i² < n 
# while n is divided by i 
# divide n by i 
# increment n 
