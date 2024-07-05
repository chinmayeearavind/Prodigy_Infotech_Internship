def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Choose the original temperature scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = int(input("Enter your choice (1/2/3): "))
    temperature = float(input("Enter the temperature value: "))

    if choice == 1:  # Celsius
        print(f"{temperature} degrees Celsius is equal to {celsius_to_fahrenheit(temperature)} degrees Fahrenheit")
        print(f"{temperature} degrees Celsius is equal to {celsius_to_kelvin(temperature)} Kelvin")

    elif choice == 2:  # Fahrenheit
        print(f"{temperature} degrees Fahrenheit is equal to {fahrenheit_to_celsius(temperature)} degrees Celsius")
        print(f"{temperature} degrees Fahrenheit is equal to {fahrenheit_to_kelvin(temperature)} Kelvin")

    elif choice == 3:  # Kelvin
        print(f"{temperature} Kelvin is equal to {kelvin_to_celsius(temperature)} degrees Celsius")
        print(f"{temperature} Kelvin is equal to {kelvin_to_fahrenheit(temperature)} degrees Fahrenheit")

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
