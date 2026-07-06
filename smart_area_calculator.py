# Smart Area Calculator
# This program calculates the area of different shapes.

print("========== SMART AREA CALCULATOR ==========")
print("1. Circle")
print("2. Rectangle")
print("3. Square")

choice = int(input("\nChoose a shape (1-3): "))

if choice == 1:
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    print(f"\nArea of the Circle = {area:.2f}")

elif choice == 2:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    area = length * breadth
    print(f"\nArea of the Rectangle = {area:.2f}")

elif choice == 3:
    side = float(input("Enter the side length: "))
    area = side * side
    print(f"\nArea of the Square = {area:.2f}")

else:
    print("\nInvalid Choice! Please run the program again.")
