import random

steps = 10000
Trials = 1000

for i in range(Trials):
    final_disp = sum(random.choice([-1, 1]) for _ in range(steps))
    print(f"Final Displacement after trial {i}: {final_disp}")
