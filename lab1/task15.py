def list_operations(numbers):
    if not numbers:
        return []

    total_sum = sum(numbers)
    min_value = min(numbers)
    max_value = max(numbers)

    squared_list = [x ** 2 for x in numbers]

    return [total_sum, min_value, max_value, squared_list]

numbers_list = [1, 2, 3, 4, 5]
result_list = list_operations(numbers_list)
print("Sum:", result_list[0])
print("Minimum:", result_list[1])
print("Maximum:", result_list[2])
print("Squared List:", result_list[3])
