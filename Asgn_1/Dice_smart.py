import random

rolls = 1000
freq = {i: 0 for i in range(1, 7)}

for _ in range(rolls):
    freq[random.randint(1, 6)] += 1

print("Frequencies:")
for face in range(1, 7):
    print(f"{face}: {freq[face]}")
