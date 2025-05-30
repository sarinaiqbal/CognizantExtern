tup = ("Interstellar", "Faded", "Harry Potter")

print(f"Favorite things: {tup}") # Print the tuple

# try-except block to catch error when trying to change tuple
try:
    tup[0] = "Tenet" # Attempt to change first element of tuple, this gives a TypeError
except:
    print("Oops, tuples cannot be changed.") # Except to catch the TypeError and display a failure message

# Length of tuple
print("Length of tuple:",len(tup))