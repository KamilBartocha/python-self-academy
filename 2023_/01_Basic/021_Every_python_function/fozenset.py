"""
frozenset() - class
Return a new frozenset object - immutable version of set.
Can be used as keys in dictionary.
"""

lst = [1, 2, 3]
s = set(lst)
s.add(4)

print(s)

frozen_s = frozenset(lst)
print(frozen_s)