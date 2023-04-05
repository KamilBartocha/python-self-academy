age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Tenary operator

message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# Chaining comparison operator -> Math syntax works

age = 22
if age >=18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")