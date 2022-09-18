#05
try:
    age = int(input('Age:'))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0')
except ValueError:
    print('invalid value')
#comments in hash
print('Sky is the limit')

numbers = [1,2,3]

class Point:
    #construktor
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print('draw')

point1 = Point()
point1.draw()
point1.move()

point1.x = 10
point1.y = 20

point2 = Point(10,14)

class Person:
    def __init__(self,name):
        self.name = name
    def Talk(self):
        print('hi')


person1 = Person(Kamil)
