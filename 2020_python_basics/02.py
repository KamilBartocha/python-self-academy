import math

print(10%2)
x = 10
x = x+3
print(x)
x += 4
print(x)
y = 2.9
print(round(y))
print(math.cos(4))

is_hot = True
is_cold = True

if is_hot:
    print('its a hot day')
elif is_cold:
    print('wear warm clothes')
else:
    print('its a graet day')

has_good_credit = True
has_high_income = True

if has_good_credit and has_high_income:
    print('Eligible for loan')
if has_good_credit or has_high_income:
    print('Eligible for loan')
if has_good_credit and not has_high_income:
    print('Eligible for loan')

temp = 30

if temp > 30:
    print('its a hot day')
elif temp < 10:
    print('its a cold day')
else:
    print('its a perfect day')

weight = int(input('Weight: '))
unit = input('L or KG ')

if unit.upper() == "L":
    print(f"you are {weight*0.45} kilos")
elif unit.upper()=="K":
    print(f"You are {weight/0.45} lbs")
else:
    print('wrong input bro')

i = 1
while i < 5:
    print('*'* i)
    i += 1

secret_number = 9
i = 0
guess = 0
while i < 3:
    guess = int(input('guess: '))
    i += 1
    if guess == secret_number:
        print('Great!')
    else:
        if i<3:
            print('try one more time')
        else:
            print('you have no more of chances :(')
