x =5
y = 9

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

print(add(x,y))
print(subtract(x,y))
print(multiply(x,y))
print(divide(x,y))