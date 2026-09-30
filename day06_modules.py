
import math
import random

print(math.sqrt(144))

number = random.randint(1, 100)

print("Random number:", number)


print(math.pow(2, 3))

print(math.sqrt(81))
number=random.randint(1,50)
print("Random number:",number)
print(math.pow(5,2.0))


try:
    number1=int(input("Enter a number: "))
    print("You entered:", number1)
except:
    print("Invalid input. Please enter a valid integer.")   
    
    

try:
    firstnumber = int(input("Enter the first number: "))
    secondnumber = int(input("Enter the second number: "))
    
    

    result = firstnumber / secondnumber

    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")