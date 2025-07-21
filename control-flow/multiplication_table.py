# This code snippet for calculating a multiplication table demonstrates the use of a for loop to iterate through numbers and print their products.
# it takes user output for the multiplication table.


print("Multiplication Table")
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i}  = {number * i}")

