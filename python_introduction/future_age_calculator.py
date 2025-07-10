#Future age calculator
# This program calculates the future age of a person based on their current age and the number of years they want to add.

# Prompt the user to input their current age with the question: “How old are you? ”

current_age = int(input("How old are you? "))
# Prompt the user to input the number of years they want to add with the question: “How many years do you want to add? ”

current_year = 2025
future_year = 2050

future_age = current_age + (future_year - current_year)
print("In the year " + str(future_year) + ", you will be " + str(future_age) + " years old.")