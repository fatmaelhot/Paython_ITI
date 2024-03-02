def filterandSquare(input_list):
    result = [(x ** 2) for x in input_list if x % 2 != 0]
    return result

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filterandSquare(mylist)
print("Result:", result)
