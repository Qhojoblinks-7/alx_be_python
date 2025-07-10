# Personal Finance Calculator
# This program calculates the total amount of money saved in a year based on monthly savings and annual interest rate.
#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).



monthlyIncome = float(input("Enter your monthly income: "))
monthlyExpenses = float(input("Enter your monthly expenses: "))

monthlySavings = monthlyIncome - monthlyExpenses
annualSavings = monthlySavings * 12
annualInterestRate = 0.05  # 5% annual interest rate
totalSavings = annualSavings + (annualSavings * annualInterestRate)

print("Your monthly savings are: $" + str(monthlySavings))
print("Projected savings after one year, with interest, is: $" + str(annualSavings))


