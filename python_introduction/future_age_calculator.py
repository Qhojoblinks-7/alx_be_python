#Future age calculator
# This program calculates the future age of a person based on their current age and the number of years they want to add.

# Prompt the user to input their current age with the question: “How old are you? ”

currentAge = int(input("How old are you? "))
# Prompt the user to input the number of years they want to add with the question: “How many years do you want to add? ”

currentYear = 2025
futureYear = 2050

futureAge = currentAge + (futureYear - currentYear)
print("In the year " + str(futureYear) + ", you will be " + str(futureAge) + " years old.")