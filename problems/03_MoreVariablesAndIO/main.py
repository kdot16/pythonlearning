# You can probably do all 5 of the problem in this one file.

print('Hello Problem 3')

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius

area = 3.14 * radius ** 2

circumference = 2 * (3.14) * radius

print("The diameter of a circle with radius", radius, "is", diameter)
print("The circumference of a circle with radius", radius, "is", circumference)
print("The area of a circle with radius", radius, "is", area)


# Get user input for the number
number = int(input("Enter an integer: "))

# Check if the number is odd or even
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")


# Print table header
print("Number\tSquare\tCube")

# Calculate and print squares and cubes for numbers 1 through 5
for number in range(1, 6):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")

    # Separate digits in an integer
num = int(input("Enter a 5-digit integer: "))
digits = [int(d) for d in str(num)]
print("Separated digits:", *digits)

# Sort numbers in ascending order
numbers = []
for i in range(3):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
sorted_numbers = sorted(numbers)
print("Numbers in ascending order:", *sorted_numbers)