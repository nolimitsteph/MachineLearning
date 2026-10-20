from math import sqrt
from DescriptiveStats.mean import calculate_mean

def calculate_standardDev(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    mean = calculate_mean(numbers)

    squaredDifferences = [(number - mean)**2 for number in numbers]

    variance = sum(squaredDifferences) / len(numbers)
    return sqrt(variance)