def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    return max(numbers) - min(numbers)