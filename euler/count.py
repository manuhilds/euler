"""
1-9
10-19
20-/10-90 + 1-9
100
1-9+ 100+ 10-19 +(20-/10-90 +1-9)
1000
"""
onetonine ='onetwothreefourfivesixseveneightnine' 
tentonine= 'teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen' 
twentytonine = 'twentythirtyfortyfiftysixtyseventyeightyninety' 

one= len(onetonine)
two= len(tentonine)
three= len(twentytonine)
som=one+two+three*(1+one)+(one + len('hundred')+3)*(two+three*(1+one))+len('onethousand')
print som
