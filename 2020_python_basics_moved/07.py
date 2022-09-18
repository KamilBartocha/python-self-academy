import random
from pathlib import Path
import openpyxl as xl
path = Path("Ecomemrce")
print(path.exists())

print('hello')
#Random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))


members = ['John','Marry','Bob']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())

#working with excel spreadsheet

wb = xl.load_workbook('path')
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
import random
from pathlib import Path
import openpyxl as xl
path = Path("Ecomemrce")
print(path.exists())

print('hello')
#Random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))


members = ['John','Marry','Bob']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())

#working with excel spreadsheet

wb = xl.load_workbook('path')
sheet = wb['Sheet1']
cell = sheet.cell(1, 1)
