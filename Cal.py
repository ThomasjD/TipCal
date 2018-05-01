#Tip calculator

#Enter the total amount
subtotal = float(input("Please enter total amount for dinner."))


#enter the tip percentage amount
percentage = float(input("Please enter tip percentage of meal.")) * .01
factor = float(1 + percentage)

#calculate tip amount & di
total = round(subtotal * factor, 2)

#Display it to User
print(f"The total amount of your bill is {total}")
