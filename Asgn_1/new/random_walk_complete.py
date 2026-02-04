import random

# -------------------------------------------------
# Function: 1D Random Walk
# -------------------------------------------------
def random_walk_1d(steps):
    """
    Performs a 1D random walk.
    Stores and returns the position at each step.
    """
    position = 0
    positions = [position]   # store positions

    for i in range(steps):
        step = random.choice([-1, 1])   # move left or right
        position = position + step
        positions.append(position)

    return positions


# -------------------------------------------------
# Main Program
# -------------------------------------------------
steps = 100        # number of steps per walk
trials = 1000      # number of trials

final_positions = []   # store final displacement of each trial

# Run multiple trials
for i in range(trials):
    positions = random_walk_1d(steps)
    final_positions.append(positions[-1])   # final displacement

# -------------------------------------------------
# Compute statistics of final displacement
# -------------------------------------------------
# Mean
total = 0
for x in final_positions:
    total = total + x
mean = total / trials

# Variance
var_sum = 0
for x in final_positions:
    var_sum = var_sum + (x - mean) ** 2
variance = var_sum / trials

# -------------------------------------------------
# Output
# -------------------------------------------------
print("Number of steps:", steps)
print("Number of trials:", trials)
print("Mean final displacement:", mean)
print("Variance of final displacement:", variance)
