"""
Author: Sarina Iqbal
Python Project: Implement Your own Data Structures
"""

inventory = {} #initialize empty inventory

print("Welcome to the Inventory Manager!")
print("Current inventory:")

# Adding 3 items to inventory
inventory["apple"] = (23, 6.50)
inventory["pear"] = (7, 8.99)
inventory["cherry"] = (46, 3.75)

for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")

print("\n") # Newline for easier view

# Adding 1 new item to inventory
print("Adding a new item: melon")
inventory["melon"] = (12, 9.60)
print("Updated inventory:")

for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")

print("\n") # Newline for easier view

# Removing 1 item from inventory
print("Removing an item: pear")
del inventory["pear"]
print("Updated inventory:")

for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")

print("\n") # Newline for easier view

# Updating price of 1 existing item
print("Updating price of apple: ")
inventory.update({"apple":(23, 7.24)})
print("Updated inventory:")

for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")

print("\n") # Newline for easier view

total = 0 # plceholder for the total value of the inventory
for item in inventory:
    # Calculate and display the total value of the inventory by multiplying the quantity and price of each item
    total += inventory[item][0] * inventory[item][1]
print(f"Total value of inventory: ${total: .2f}") # Round total to 2 decimal places

