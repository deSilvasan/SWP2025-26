import random
import sys

def fill_array_numbers(upper_limit):
    # Return a list containing numbers from 1 up to upper_limit (inclusive)
    return list(range(1, upper_limit + 1))

def generate_random_numbers(output_array, moves):
    # Draw 'moves' random numbers from output_array WITHOUT replacement
    # random.sample returns a new list of unique elements
    return random.sample(output_array, moves)

def frequencies_random_numbers(array, statistic_array):
    # Count the occurrences of each number in the drawn array
    # statistic_array is a list where index corresponds to the number
    for element in array:
        statistic_array[element] += 1

def relative_frequency_random_numbers(statistic_array, total_withdrawals):
    # Convert absolute counts into relative frequencies by dividing by total draws
    for i in range(len(statistic_array)):
        statistic_array[i] /= total_withdrawals

def main():
    # Read command-line arguments:
    # upper_limit_numbers: maximum number in the range (e.g. 45)
    # random_numbers_count: how many numbers to draw each time (e.g. 6)
    # moves: how many times to repeat the drawing (e.g. 1000)
    upper_limit_numbers = int(sys.argv[1])
    random_numbers_count = int(sys.argv[2])
    moves = int(sys.argv[3])

    # Initialize statistic array to count occurrences for each number (index 0 unused)
    statistic_array = [0] * (upper_limit_numbers + 1)

    # Repeat the drawing process 'moves' times
    for _ in range(moves):
        # Create a fresh list of numbers 1..upper_limit_numbers
        output_array = fill_array_numbers(upper_limit_numbers)
        # Draw random_numbers_count unique numbers from the list
        drawn_numbers = generate_random_numbers(output_array, random_numbers_count)
        # Count frequencies of the drawn numbers
        frequencies_random_numbers(drawn_numbers, statistic_array)

    print("How often each number was drawn:")
    # Print counts for numbers 1 through upper_limit_numbers (ignore index 0)
    print(statistic_array[1:])

    # Calculate total number of numbers drawn (moves times numbers per draw)
    total_draws = moves * random_numbers_count
    # Convert counts to relative frequencies (probabilities)
    relative_frequency_random_numbers(statistic_array, total_draws)

    print("\nRelative frequencies:")
    print(statistic_array[1:])

    # Create a dictionary mapping number to relative frequency
    freq_dict = {i: statistic_array[i] for i in range(1, upper_limit_numbers + 1)}
    # Sort the dictionary by frequency (lowest to highest)
    sorted_freq = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
    print("\nSorted frequencies:")
    print(sorted_freq)

if __name__ == "__main__":
    main()
