import random

# =========================================================
# FUNCTION 1: Single 1D Random Walk
# =========================================================
def random_walk_1d(steps):
    """
    Performs one 1D random walk.
    Returns final position and full trajectory.
    """

    position = 0          # start at origin
    trajectory = [position]

    for i in range(steps):
        step = random.choice([-1, 1])   # move left or right
        position = position + step
        trajectory.append(position)

    return position, trajectory


# =========================================================
# FUNCTION 2: Multiple Random Walks
# =========================================================
def multiple_random_walks(steps, trials):
    """
    Performs multiple 1D random walks.
    Returns list of final positions.
    """

    final_positions = []

    for i in range(trials):
        position = 0
        for j in range(steps):
            position = position + random.choice([-1, 1])
        final_positions.append(position)

    return final_positions


# =========================================================
# FUNCTION 3: Mean and Variance
# =========================================================
def mean_and_variance(data):
    """
    Computes mean and variance of a list.
    """

    total = 0
    for x in data:
        total = total + x
    mean = total / len(data)

    var_sum = 0
    for x in data:
        var_sum = var_sum + (x - mean) ** 2
    variance = var_sum / len(data)

    return mean, variance


# =========================================================
# MAIN PROGRAM (EDIT ONLY THIS PART IN EXAM)
# =========================================================
steps = 100        # number of steps
trials = 1000      # number of walks

# ---- Single walk ----
final_pos, path = random_walk_1d(steps)
print("Single Walk Final Position:", final_pos)
print("Trajectory:", path)

# ---- Multiple walks ----
results = multiple_random_walks(steps, trials)
print("\nFinal positions of all walks:")
print(results)

# ---- Statistics ----
mean, variance = mean_and_variance(results)
print("\nMean of final positions:", mean)
print("Variance of final positions:", variance)
