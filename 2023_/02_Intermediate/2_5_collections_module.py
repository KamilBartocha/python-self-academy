from collections import namedtuple

# read only class/object
FullName = namedtuple("FullName", ("first", "middle", "last"))

my_name = FullName("Monty", "Python", "snake")

print(my_name[0])
print(my_name.first)

# my_name[0] = "Conty" -> TypeError, FullName does not support item assignment

# there are more collection useful techniques, but for now I'm not interested
# in them. Maybe in future :)