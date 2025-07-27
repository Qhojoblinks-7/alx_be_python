from datetime import datetime, timedelta;
'''
This module provides a function to store and display the current date and time in a human readable way.
It uses the datetime module to get the current date and time and formats it into a readable string
'''

def display_current_datetime():
    """
    Displays the current date and time in a formatted string.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_datetime}")

display_current_datetime()


'''
calculate_future_date: this function takes a number of days as input and calculates the date that many days in the future.
It uses the datetime module to add the specified number of days to the current date and returns the future date in a formatted string.
'''
def calculate_future_date(days):
    """
    Calculates the date that many days in the future from today.
    
    :param days: Number of days to add to the current date.
    :return: Future date in a formatted string.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

days = input("Enter the number of days to add to the current date: ")
try:
    days = int(days)
except ValueError:
    print ("Error: Please enter a valid integer for the number of days.")
print(f"Future Date: {calculate_future_date(days)}")


'''
commit message: feat: create a new function that performs a simple operation based on an accepted operation name
This function performs a simple arithmetic operation based on the operation name provided by the user.
It uses a match-case structure to determine the operation and returns the result.'''