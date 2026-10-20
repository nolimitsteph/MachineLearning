def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    return sum(numbers) / len(numbers)
