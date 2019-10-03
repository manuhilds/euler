j = 10000
def yes(n):
    for x in range(1, n):
        for z in range(1, x):
            for y in range(1, z):
                if x*x == (z*z+y*y):
                    if x+y+z == 1000:
                        print (x,y,z)
                        print(x*x,y*y,z*z)
                        print(x*y*z)
                        return 0
        

 
yes(j)
