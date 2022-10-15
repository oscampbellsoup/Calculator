# Import calculator art.
from calculator_art import logo
print(logo)

# Define operation check function.
def operation_check(n):
    if operation == operations_list[n]:
        return True
    
# CLS commands do not work with IDE used to write this program. clear function used as substitute.
def clear():
    print ("\n" * 100)
    
# Define addition function.
def add(a, b):
    return a + b

# Define subtraction function.
def subtract(a, b):
    return a - b

# Define multiplication function.
def multiply(a, b):
    return a * b

# Define division function.
def divide(a, b):
    return a / b

# Output function.
def output(a, b):
    global operation_todo
    if operation_todo == 0:
        output = add(a, b)
    elif operation_todo == 1:
        output = subtract(a, b)
    elif operation_todo == 2:
        output = multiply(a, b)
    elif operation_todo == 3:
        output = divide(a, b)
    print(f"{a} {operations_list[operation_todo]} {b} = {output}")
    return output

# Continue function.
def continue_(x):    
    while True:
        yes_or_new = input(f"Type 'y' to continue calculating with {x} or type 'n' to start a new calculation: ").lower()
        if yes_or_new == 'y':
            return True
        elif yes_or_new == 'n':
            return False
        else:
            print("Sorry, I did not understand that.")

while True:             
# While loop conditon for first and new calculations.
    calculation_continue = False
    
# Operation list defined to check inputs.
    operations_list = ['+', '-', '*', '/']
    
# 'y' or 'n' list defined to check inputs.
    yes_or_new_list = ['y', 'n']
    
    while calculation_continue == False:
        a = int(input("What's the first number?: "))
        print("+\n-\n*\n/")
        calculation_continue = True
        
    while calculation_continue == True:       
        while True:
            operation = input("Pick an operation: ")
            if operation_check(0) == True:
                operation_todo = 0
                break
            elif operation_check(1) == True:
                operation_todo = 1
                break
            elif operation_check(2) == True:
                operation_todo = 2
                break
            elif operation_check(3) == True:
                operation_todo = 3
                break
            else:
                print("Sorry, I did not understand that.")
        b = int(input("What's the next number?: "))
        x = output(a, b)
        y = continue_(x)
        if y == True:
            calculation_continue = True
        elif y == False:
            break
        if calculation_continue == True:
            a = x
    
        
    

