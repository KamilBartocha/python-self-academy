"""
list comprehension =  a way to create a new list with less syntax
                      can mimic certain lambda functions, easier to read
                      list = [expression for item in iterable]
                      list = [expression for item in iterable if conditional]
                      list = [expression if/else for item in iterable]
"""


squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

# list comprehension with the same example
squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]

passed_students_lambda = list(filter(lambda x: x >= 60, students))
passed_students_c = [i for i in students if i >= 60]
passed_students_c2 = [i if i >= 60 else "FAILED" for i in students]

print(passed_students_lambda)
print(passed_students_c)
print(passed_students_c2)



"""dictionary comprehension = create dictionaries using an expression
                           can replace for loops and certain lambda functions

dictionary = {key: expression for (key,value) in iterable}
dictionary = {key: expression for (key,value) in iterable if conditional}
dictionary = {key: (if/else) for (key,value) in iterable}
dictionary = {key: function(value) for (key,value) in iterable}"""

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)


weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)