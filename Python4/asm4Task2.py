info = {"name": "Sarina", "age":21, "city": "Tucson"}

print(info)

info["favorite color"] = "blue"

info.update({"city":"Tampa"})

print(info)

print("Keys: ")
for key in info:
    print("-", key, end=" ")
print(" ")

print("Values:")
for key, value in info.items():
    print("-", value, end=" ")