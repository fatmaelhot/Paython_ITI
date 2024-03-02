def checkExistKeys(dictionary):
    keychecked = ["job", "card_number"]
    for key in keychecked:
        if key not in dictionary:
            return False
    return True

myDictionary = {"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"}
result = checkExistKeys(myDictionary)
print(result)  