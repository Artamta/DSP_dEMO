import random
rolls=1000
rolls_list=[]
for i in range(rolls):
	a=random.randint(1,6)
	rolls_list.append(a)
#Count Frequencies
n=len(rolls_list)
a=b=c=d=e=f=0
for i in range(n):
    if rolls_list[i]==1:
        a = a+1
    elif rolls_list[i]==2:
        b= b+1
    elif rolls_list[i]==3:
        c=c+1
    elif rolls_list[i]==4:
        d=d+1
    elif rolls_list[i]==5:
        e=e+1
    else:
        f=f+1
print("Frequinces:")
print(a)

