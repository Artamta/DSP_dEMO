#importing_random_module

import random

steps=100
print("I am using steps :",steps)
Trials=100
print("Trial_Runs",Trials)
D=[]
for i in range(Trials):
    c=0
    lst=[]
    for k in range(steps):
	    a=random.choice([-1,1])
	    lst.append(a)

    n=len(lst)
    for j in range(n):
	    c=c+lst[j]
    D.append(c)
l=len(D)
for i in range(l):
    d=0
    #print("Final Displacement after step",D[i])
    d=d+D[i]
print("Final Stats added val :",d )
