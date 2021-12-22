#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

print("Welcome to the Tip Calculator!")
bill = float(input("What was the Total Bill? $"))
tip =  int(input("How much Tip would you like to Give? 10, 12, Or 15? "))
people =  int(input("How many People to Split the Bill? "))


tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should Pay: ${final_amount}")