# This program will calculate your bill, based on how much tip you want to pay
print("Welcome to the tip calculator")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What is the tip percentage you want to give? 10, 12, 15: "))
people = int(input("How many people to split the bill? "))

# Calculate the total bill with tip
tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount

# Calculate how much each person should pay
amount_per_person = total_bill / people

# Format to 2 decimal places
print(f"The total bill including tip is: ${total_bill:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")

