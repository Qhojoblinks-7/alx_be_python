# Personal Finance Calculator
# This program calculates the total amount of money saved in a year based on monthly savings and annual interest rate.
#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).



monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
annualSavings = monthly_savings * 12
annualInterestRate = 0.05  # 5% annual interest rate
totalSavings = annualSavings + (annualSavings * annualInterestRate)

print("Your monthly savings are: $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(annualSavings))


