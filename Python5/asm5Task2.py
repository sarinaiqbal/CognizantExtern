'''
Author: Sarina Iqbal
Assignment: About Parameters of Functions
Task 2
'''

def describe_pet(pet_name, animal_type="dog"):
    print("I have a " + animal_type + " named " + pet_name + ".")



describe_pet("Sam") # Calling function with pet name Sam (default type is dog)
describe_pet("Mary", "cat") # Calling function with pet name Mary and type cat