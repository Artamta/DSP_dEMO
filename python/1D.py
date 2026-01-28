steps=10000
list=[]
import random
for i in range(steps):
	s=random.choice([-1,1])
	list.append(s)
n=len(list)
add=0
for i in range(n):
	add+=list[i]
print(add)
