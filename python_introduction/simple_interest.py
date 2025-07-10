# ( I ) is the interest earned,
# ( P ) is the principal amount (initial investment),
# ( R ) is the annual interest rate (as a decimal),
# ( T ) is the time the money is invested for in years.

principal = 1000  # Principal amount
rate = 0.05  # Annual interest rate (5%)
time = 3     # Time in years

interest = principal * rate * time  # Simple interest formula
# Print the result
print("The simple interest earned on an investment of $" + str(principal) +
      " at an annual interest rate of " + str(rate * 100) + "%" +
      " over " + str(time) + " years is $" + str(interest))