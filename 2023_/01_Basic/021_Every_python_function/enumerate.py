"""
enumerate(), enumerate(itrable, start=0)
Return an enumerate object. Iterable must be z sequence, iterator or any
object which supports iteration
"""

values = ["a", "b", "c", "d", "f"]

for index, value in enumerate(values):
    print(f"Index is: {index}, and value: {value}")

print(list(enumerate(values)))