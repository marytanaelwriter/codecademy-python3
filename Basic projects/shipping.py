# Sal's Shipping Project <3

# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

# Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

# Code begins here

weight = 41.5

# Ground Shipping

ground_cost = ""

if weight <= 2:
  ground_cost = ((weight * 1.5) + 20)
elif weight > 2 and weight <= 6:
  ground_cost = ((weight * 3) + 20)
elif weight > 6 and weight <= 10:
  ground_cost = ((weight * 4) + 20)
else:
  ground_cost = ((weight * 4.75) + 20)

print("GROUND SHIPPING")
print(f"Your total shipping cost is $ {ground_cost}.")

# Ground Shipping Premium

premium_cost = weight + 125

print("GROUND SHIPPING PREMIUM")
print(f"Your total shipping cost is $ {premium_cost}.")

# Drone Shipping

drone_cost = ""

if weight <= 2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25

print("DRONE SHIPPING")
print(f"Your total shipping cost is $ {drone_cost}.")
