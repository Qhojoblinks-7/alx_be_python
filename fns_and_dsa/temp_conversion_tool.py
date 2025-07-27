# This script is used to convert temperatures between Celsius and Fahrenheit.
# It provides a simple command-line interface for users to input temperatures and choose the conversion direction.

'''
this script is used to convert temperatures between Celsius and Fahrenheit.
It provides a simple command-line interface for users to input temperatures and choose the conversion direction.
'''


FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

FAHRENHEIT_TO_CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Matches: (\w+ - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  # Matches: (value * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    while True:
        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        input = float(input("Enter the temperature to convert:"))

        if choice == 'F':
            
            celsius = convert_to_celsius(input)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")

        elif choice == 'C':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_to_fahrenheit(input)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

