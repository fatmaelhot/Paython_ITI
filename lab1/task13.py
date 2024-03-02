import math

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

num1 = 7
num2 = 10
print(num1, "is prime:", isPrime(num1))
print(num2, "is prime:", isPrime(num2))
