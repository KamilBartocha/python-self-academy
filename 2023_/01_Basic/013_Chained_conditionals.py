# Chainted contitionals:
# and, or, not
# and - math logic AND operator
print(True and True) # -> True
print(True and False) # -> False
print(False and True) # -> False
print(False and False) # -> False

# or - math logic OR operator
print(True or True) # -> True
print(True or False) # -> True
print(False or True) # -> True
print(False or False) # -> False

# not - math negation operator

print(not True) # -> False
print(not False) # -> True

# Example

age = 16
is_in_school = True

while(age == 16 and is_in_school):
    print("In school still and 16")
    choice = input("Are you still in school? (n/y): ")
    if(choice.lower() == "n"):
        is_in_school = False

is_high_income = False
is_good_credit = True
is_student = True

if is_high_income and is_good_credit and not is_student:
    print("Eligible")

if is_high_income or is_good_credit and not is_student:
    print("Eligible")