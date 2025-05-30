'''
Author: Sarina Iqbal
Python Assignment: Hands on Python Data Structures
Task 2
'''

# Creating dictionary info
info = {"name": "Sarina", "age":21, "city": "Tucson"}

# Add a new key value pair
info["favorite color"] = "blue"

# Update 'city' key with new value
info.update({"city":"Tampa"})

# Printing keys
print("Keys: ")
for key in info:
    print("-", key, end=" ") # all keys in same line with a preceding '-'
print(" ")

# Printing values
print("Values:")
for key, value in info.items():
    print("-", value, end=" ") # all keys in same line with a preceding '-'
