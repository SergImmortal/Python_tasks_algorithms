from timing import timing

print('{color}Recursion solution for factorial.{endcolor}\n'.format(color='\033[42m', endcolor='\033[0m'))

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

@timing
def alias(x):
    return factorial(x)
print(str(alias(200)) + "\n")

print('{color}Cycle solution for factorial.{endcolor}\n'.format(color='\033[42m', endcolor='\033[0m'))
print('{color}Cycle WHILE:{endcolor}\n'.format(color='\033[42m', endcolor='\033[0m'))

@timing
def factorialWhile(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

print(str(factorialWhile(200)) + "\n")
print('{color}Cycle FOR:{endcolor}\n'.format(color='\033[42m', endcolor='\033[0m'))

@timing
def factorialFor(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

print(str(factorialFor(200)) + "\n")