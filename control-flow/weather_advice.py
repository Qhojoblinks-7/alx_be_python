# The following code snippet demonstrates a simple weather recommendation system using if-elif-else statements.
# It takes user input for the weather condition and provides appropriate clothing suggestions.# This code snippet is a simple calculator using match-case statements to perform basic arithmetic operations.

weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
    
    # fix: changed the input variable to 'weather' for 
    # ref: 
    # feat: