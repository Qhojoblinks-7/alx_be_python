# fruits = ["mango", "banana", "apple", "orange", "grape"]
# print("Fruits in the list:")
# print(fruits[1])

# mySelf ={
#     "name": "Immanuel",
#     "age": 20,
#     "country": "Nigeria",
#     "hobby": "coding"
# }

# print(mySelf.values())
# print(mySelf.get("name", "Not found"))

def randomNumbers ():
    import random
    numbers = set()
    while len(numbers) < 10:
        numbers.add(random.randint(0, 11))
    return numbers
print(randomNumbers())