# Random 2 Digit Number. Something like 39.
# Code you will write will be able to add 1st & 2nd Digit & end up with a Numerical Result.

# Eg: 39 (3 + 9 = 12).
# Use Type Checking & Conversion & Everything you learned before.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Two Digit Number - Could be anything (Str/Int/Float)
# First - Check the data type of two_digit_number
# Print(type(two_digit_number))

# Strings can do Subscripting.
# Get the first & Second digits using Subscripting them.
# Then convert String to int.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Add the two digits together
result = int(first_digit) + int(second_digit)
print(result)