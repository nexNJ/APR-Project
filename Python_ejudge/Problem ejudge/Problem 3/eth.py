numbers = []

while True:
    x = input("Enter a number (or '$' to finish): ")

    if x == "$":
        break

    try:
        num = int(x)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number or '$' to finish.")

if numbers:
    min_value = min(numbers)
    max_value = max(numbers)
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
else:
    print("No numbers entered.")
