# 🚨 Don't change the code below 👇
height = input("Enter your Height in M: ")
weight = input("Enter your Weight in Kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Check the data type & Change the data type as required

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
