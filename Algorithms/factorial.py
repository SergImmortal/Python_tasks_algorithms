from timing import timing

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

@timing
def factorialRecursive(x):
    return factorial(x)

@timing
def factorialWhile(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

@timing
def factorialFor(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

if __name__ == '__main__':

    print('{color}Recursion solution for factorial.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    print(str(factorialRecursive(200)) + "\n")
    print('{color}Cycle solution for factorial.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    print('{color}Cycle WHILE:{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    print(str(factorialWhile(200)) + "\n")
    print('{color}Cycle FOR:{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    print(str(factorialFor(200)) + "\n")