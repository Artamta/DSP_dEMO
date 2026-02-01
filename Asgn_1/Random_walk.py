import random

#function for random walk
steps=10000
list=[]
b=[]
disp=10
c=0
for i in range(disp):
	for i in range(steps):
		a=random.choice([-1,1])
		list.append(a)
	n=len(list)

	for j in range(n):
		c=c+list[j]
b.append(c)
n=len(b)
for i in range(n):
	print(b[i])
