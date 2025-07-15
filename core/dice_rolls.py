import random

LOWER_BOUND = 1
UPPER_BOUND = 6
NUM_ROLLS = 3

def roll_dice(lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    """Roll a dice with specified lower and upper bounds."""
    if lower_bound >= upper_bound:
        raise ValueError("Lower bound must be less than upper bound.")
    return random.randint(lower_bound, upper_bound)

def roll_multiple_dice(num_rolls=NUM_ROLLS, lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND):
    """Roll multiple dice and return the results."""
    if num_rolls <= 0:
        raise ValueError("Number of rolls must be a positive integer.")
    results = []
    for i in range(num_rolls):
        result = roll_dice(lower_bound, upper_bound)
        results.append(result)
    return results

def take_average(rolls):
    """Calculate the average of a list of rolls."""
    if not rolls:
        raise ValueError("Rolls list cannot be empty.")
    return sum(rolls) / len(rolls)

def sort_descending_rolls(rolls):
    """Sort the rolls in descending order."""
    return sorted(rolls, reverse=True)

def print_sorted_rolls(rolls):
    """Print the sorted rolls."""
    sorted_rolls = sort_descending_rolls(rolls)
    print("Rolls in descending order:")
    for i, roll in enumerate(sorted_rolls, start=1):
        print(f"Roll {i}: {roll}")

def main():
    """Main function to roll dice and calculate the average."""
    try:
        rolls = roll_multiple_dice()
        average = take_average(rolls)
        print(f"Average of dice rolls: {average:.2f}")
        print_sorted_rolls(rolls)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()