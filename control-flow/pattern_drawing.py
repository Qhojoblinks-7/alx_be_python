# This code snippet is a simple pattern drawing program that uses nested loops to create a grid of asterisks.
# It takes user input for the size of the grid and prints a pattern accordingly.
# It uses a while loop to iterate the rows and a for loop to iterate the * characters in each row.

print("Pattern Drawing")
size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    col = 0
    for col in range(size):
        print("*", end=" ")
    print()  # Move to the next line after printing one row
    row += 1
    
# commit messages
# feat: Implemented a pattern drawing program using nested loops
# refactor: Simplified the pattern logic and improved output formatting
# docs: Added comments to explain the pattern drawing functionality3
