#Imani Hollie 02/14/2024
#This is a simulated calculator

#For inputs, ask for which function needs to be called
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        return 'Cannot divide by zero!'
    elif b == 0:
        return 'Cannot divide by zero!'
    else:
        return a / b

num1 = float(input('Enter First Number:'))
num2 = float(input('Enter Second Number:'))

print('Available Operations:')
print('1 - Add')
print('2 - Subtract')
print('3 - Multiply')
print('4 - Divide')

operation = float(input("Enter Operation Number: "))

if operation == 1:
        print(f'The sum of {num1} and {num2} is: {add(num1, num2)}')
elif operation == 2:
        print(f'The difference of the subtraction is: {subtract(num1, num2)}')
elif operation == 3:
        print(f'The multiple of {num1}: {multiply(num1, num2)}')
elif operation == 4:
        print(f'The result of the division is: {divide(num1, num2)}')
else:
      print('Invalid Operation Number')
