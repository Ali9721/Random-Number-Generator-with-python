# At first I import random.
import random

# Define "low" & "high" & "random_num" variables and use "randint"
low = int(input("Please enter the lower bound: "))
high = int(input("Please enter the upper bound: "))
random_num = random.randint(low, high)

# Output the result
print(f"Random number between {low} and {high}: {random_num}")