from timing import timing

print("Recursion solution for factorial.\n")

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

@timing
def alias(x):
    return factorial(x)
print(str(alias(200)) + "\n")


print("Cycle solution for factorial.\n")

@timing
def factorialCycle(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    else:
        return result

print(str(factorialCycle(200)) + "\n")