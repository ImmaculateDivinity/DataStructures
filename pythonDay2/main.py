#tip calculator
cost = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage_tip = tip * 0.01
people = int(input("How many people are there? "))
each_pay = round(((cost * percentage_tip + cost) / people), 2)
print(f"Each person pays ${each_pay:.2f}.")