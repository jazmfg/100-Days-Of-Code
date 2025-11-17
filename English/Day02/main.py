print("\n*** Tip Calculator ***\n")

bill = float(input("Enter the total bill: $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15%: "))
people = int(input("How many people will split the bill: "))

payment_per_person = (bill * (tip / 100 + 1)) / people

print(f"Each person should pay: ${payment_per_person:.2f}") 