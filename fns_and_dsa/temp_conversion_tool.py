FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

# check if type of temperature is a number
try:
    temperature = float(temperature)
    if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}°F")
       
    elif unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}°C")
except ValueError:
    print("Invalid temperature. Please enter a numeric value")
    exit()