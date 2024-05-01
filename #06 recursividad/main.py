"""
    Recursividad
"""

def rec_print_number(number):
    print(number)
    number -= 1
    rec_print_number(number) if number >= 0 else exit


#rec_print_number(100)

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1) 
    
#print(factorial(3))

def fibbo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibbo(number - 1) + fibbo(number - 2) 

print(fibbo(5))