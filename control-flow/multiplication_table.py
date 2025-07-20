# This code snippet for calculating a multiplication table demonstrates the use of a for loop to iterate through numbers and print their products.
# it takes user output for the multiplication table.


print("Multiplication Table")
num = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")


# commit messages
# feat: Implemented a multiplication table using nested loops
# refactor: Simplified the multiplication logic and improved output formatting