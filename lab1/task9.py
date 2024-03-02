def checkNum(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 9
result = checkNum(num)
print("The number", num, "is", result)
