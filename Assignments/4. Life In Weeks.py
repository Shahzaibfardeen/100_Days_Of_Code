# 🚨 Don't change the code below 👇
Age = input("What is your Current Age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Input - Always create a String Data Type.
Age_as_int = int(Age)
Years_Remaining = 90 - Age_as_int

# There are 365 Days in a Year.
Days_Remaining = Years_Remaining * 365

# There are 52 Weeks in a Year.
Weeks_Remaining = Years_Remaining * 52

# There are 12 Months in a Year.
Months_Remaining = Years_Remaining * 12

# Print into a String.
Message = f"You have {Days_Remaining} Days, {Weeks_Remaining} Weeks, and {Months_Remaining} Months left" 

print(Message)