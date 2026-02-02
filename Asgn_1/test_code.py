x = [1, 2]
y = [x, x]
print(y)

x.append(3)
print(y)

y[0] = [9, 9]
print(x)
print(y)
