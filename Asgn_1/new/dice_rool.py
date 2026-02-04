import random

# -------------------------------------------------
# Function: Simulate dice rolls
# -------------------------------------------------
def dice_simulation(trials):
    """
    Simulates rolling a fair six-sided die.
    Returns frequency and probability of each outcome.
    """

    # Step 1: Initialize frequency dictionary
    frequency = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    # Step 2: Perform dice rolls
    for i in range(trials):
        roll = random.randint(1, 6)
        frequency[roll] = frequency[roll] + 1

    # Step 3: Compute probabilities
    probability = {}
    for face in frequency:
        probability[face] = frequency[face] / trials

    return frequency, probability


# -------------------------------------------------
# Main Program
# -------------------------------------------------
trials = 10000   # number of dice rolls

freq, prob = dice_simulation(trials)

# -------------------------------------------------
# Output
# -------------------------------------------------
print("Number of rolls:", trials)
print("\nOutcome | Frequency | Probability")

for face in range(1, 7):
    print(face, "       ", freq[face], "       ", prob[face])
