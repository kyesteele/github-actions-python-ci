def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        print("Error: dividing by zero.")
        return None
