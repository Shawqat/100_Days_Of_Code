def add(num1, num2):
    if type(num1) == float and type(num2) == float:
        return f"{num1} + {num2} = {num1 + num2}"

def multiply(num1, num2):
    if type(num1) == float and type(num2) == float:
        return f"{num1} * {num2} = {num1 * num2}"

def subtract(num1, num2):
    if type(num1) == float and type(num2) == float:
        if num1 > num2:
            return f"{num1} - {num2} = {num1 - num2}"
        return f"{num2} - {num1} = {num2 - num1}"
    

def divide(num1, num2):
    if type(num1) == float and type(num2) == float:
        if num1 > num2:
            return f"{num1} / {num2} = {num1 / num2}"
        return f"{num2} / {num1} = {num2 / num1}"