# Task 1
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))
largest = 0
smallest = 0

if number_one > number_two and number_one > number_three:
    largest = number_one
elif number_two > number_one and number_two > number_three:
    largest = number_two
else:
    largest = number_three

# Task 2
if number_one < number_two and number_one < number_three:
    smallest = number_one
elif number_two < number_one and number_two < number_three:
    smallest = number_two
else:
    smallest = number_three
    
print(f"The largest number is {largest}. The smallest number is {smallest}.")

# Task 3

if number_one == number_two and number_one > number_three:
    print(f"Two numbers are equal and the largest: {number_one}")
elif number_two == number_three and number_two > number_one:
    print(f"Two numbers are equal and the largest: {number_two}")
elif number_three == number_one and number_three > number_two:
    print(f"Two numbers are equal and the largest: {number_three}")        
elif number_one == number_two:
    print(f"There are two equal numbers: {number_one}")
elif number_two == number_three:
    print(f"There are two equal numbers: {number_two}")
else:
    print(f"There are two equal numbers: {number_three}")


