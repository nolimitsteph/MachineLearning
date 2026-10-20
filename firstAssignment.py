# 1. Ask the user for their name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# 2. Calculate their approximate age
current_year = 2026
age = current_year - birth_year

# 3. Print a personalized message based on their age
print(f"\nHello, {name}!")
print(f"You are approximately {age} years old.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")