import random

def calculate_median(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    middle = int(n//2)

    if n % 2 == 0:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle-1] + sorted_numbers[middle]) /2

