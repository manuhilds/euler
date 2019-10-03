import math 

def get_factors(n):
    return sum(2 for i in range(1, math.ceil(math.sqrt(n)+1)) if not n % i)

def generate_triangles(limit):
    
    for l in range(1,limit):
        yield sum(range(l +1 ))

def test_triangles():
    triangles  = generate_triangles(10000000)
    for i in triangles:
        if get_factors(i)>= 500:
            return i 

print(test_triangles())