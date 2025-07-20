# The following code snippet demonstrates a simple weather recommendation system using if-elif-else statements.
# It takes user input for the weather condition and provides appropriate clothing suggestions.# This code snippet is a simple calculator using match-case statements to perform basic arithmetic operations.

weatherInput = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if weatherInput == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weatherInput == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weatherInput == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
    # commit messages
    # feat: Added a weather recommendation system based on user input