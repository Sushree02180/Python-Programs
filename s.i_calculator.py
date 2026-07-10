# Simple Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print("Simple Interest:", simple_interest)
print("Total Amount:", amount)
