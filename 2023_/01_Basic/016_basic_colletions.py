
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and unindexed, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and immutable. Duplicates OK. FASTER
#   Dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates

# list
friuts = ["apple", "banana", "tomato"]
print(len(friuts))
friuts.append("pineapple")
friuts.remove("tomato")
friuts.insert(0, "kiwi")
friuts.sort()
friuts.reverse()
# friuts.clear()
friuts.index("apple")
friuts.count("banana")

# set

friuts = {"apple", "banana", "tomato"}
friuts.add("pineapple")
friuts.remove("apple")
friuts.pop() # latest but random
friuts.clear()


# tuple

friuts = ("apple", "banana", "tomato")
friuts.count("apple")
friuts.index("apple")



# Dictionary
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Poland": "Warsaw"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
   print("That capital exists")
else:
   print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem() # remove latest key-value pair
capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
  print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
   print(f"{key}: {value}")