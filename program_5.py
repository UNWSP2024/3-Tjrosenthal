# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

#Tanner Rosenthal
#2/4/2025

print("Menu:")
food = int(input("Type 1 for a Hot Dog or 2 for a Chilli Dog"))
cheese = input("would you like cheese?")
peppers = input("Would you like peppers?")
onions = input("Would you like grilled onions?")


cheese_cost = 0.00
peppers_cost = 0.00
onions_cost = 0.00

if cheese == "yes" or " yes":
   cheese_cost = 0.50

if peppers == "yes" or " yes":
   peppers_cost = 0.75

if onions == "yes" or " yes":
   onions_cost = 1.00

if food == 1:
   dog_cost = 3.50
   topped_dog = dog_cost + cheese_cost + peppers_cost + onions_cost
   tax = topped_dog * 0.07
   rounded_tax = round(tax, 2)
   final_cost = rounded_tax + topped_dog
   print()
   print("You chose a Hot Dog")
   print("Price: $", topped_dog)
   print("Tax: $", rounded_tax)
   print("Final Price: $", final_cost)

elif food == 2:
   dog_cost = 4.50
   topped_dog = dog_cost + cheese_cost + peppers_cost + onions_cost
   tax = topped_dog * 0.07
   rounded_tax = round(tax, 2)
   final_cost = rounded_tax + topped_dog
   print()
   print("You chose a Chilli Dog")
   print(f"Price: ${topped_dog}")
   print(f"Tax: ${rounded_tax}")
   print(f"Final Price: ${final_cost}")
