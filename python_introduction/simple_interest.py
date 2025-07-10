# ( I ) is the interest earned,
# ( P ) is the principal amount (initial investment),
# ( R ) is the annual interest rate (as a decimal),
# ( T ) is the time the money is invested for in years.

P = 1000  # Principal amount
R = 0.05  # Annual interest rate (5%)
T = 3     # Time in years

I = P * R * T  # Simple Interest formula
# Print the result
print("The simple interest earned on an investment of $" + str(P) +
      " at an annual interest rate of " + str(R * 100) + "%" +
      " over " + str(T) + " years is $" + str(I))