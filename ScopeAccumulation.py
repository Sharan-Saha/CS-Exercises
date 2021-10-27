def multiply(x, y):
    result = 0
    for i in range(y):
        result += x
    
    return result

def raisePower(x, y):
    result = x
    for i in range(y - 1):
        result *= x
    
    return result

def square(x):
    result = multiply(x, x)
    return result


def main():
    print(multiply(4, 0))

main()