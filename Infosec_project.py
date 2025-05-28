# Question 1 : Write a program that asks the
#  user for a number of days. The program
# then prints out the number of seconds
#  in the number of days given.

days = int(input("Enter the number of days: "))
seconds = days * 24 * 60 * 60
print(f"There are {seconds} seconds in {days} days.")


# Question 2:calculating the volume of a sphere 
import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * (radius ** 3)
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")


def compute_area(side):
    return side ** 2

def compute_perimeter(side):
    return 4 * side

side = float(input("Enter the side length of the square: "))
area = compute_area(side)
perimeter = compute_perimeter(side)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Question 4: functions that determines whether a character 
#input by a user is uppercase or lower case. 
def check_case(char):
    if char.isupper():
        print(f"The character '{char}' is uppercase.")
    elif char.islower():
        print(f"The character '{char}' is lowercase.")
    else:
        print(f"The character '{char}' is not a letter.")

char = input("Enter a character: ")
check_case(char)

# Question 5:Rewriting a pseudocode in python 
x = 0
y = 20

while y >= 6:
    y = y - 4
    if y != 0:
        x = x + (2 / y)

print(f"The final value of x is {x}")

# Question 6 (i):
#Using a loop for a user to continually input 5 values to populate an 
#array.

values = []  

for i in range(5): 
    value = float(input(f"Enter value {i + 1}: "))  
    values.append(value)  

# (ii)Calculate and display
# the average of the values input into the 
#array. 
average = sum(values) / len(values)
print(f"The average of the values is {average:.2f}")
