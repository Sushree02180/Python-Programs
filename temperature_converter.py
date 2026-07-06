# Temperature Converter

print("========== TEMPERATURE CONVERTER ==========")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("\nEnter your choice (1-2): "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"\n{celsius}°C = {fahrenheit:.2f}°F")

elif choice == 2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"\n{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("\nInvalid choice! Please run the program again.")
