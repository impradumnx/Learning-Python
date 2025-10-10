# Program to find the sum of numbers up to n

# Take input from the user
n = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Use a loop to add numbers from 1 to n
for i in range(1, n + 1):
    total += i

# Display the result
print(f"The sum of numbers from 1 to {n} is: {total}")
