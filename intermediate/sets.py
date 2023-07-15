myset = {1, 2, 3, 4}
myset2 = set([2, 3, 4, 5])
myset3 = set("Hello")


print(myset)
print(myset2)
print(myset3)


myset4 = {}
myset5 = set()

print(type(myset4))
print(type(myset5))

odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}

u = odd.union(even)
print(u)

i = odd.intersection(odd)
print(i)


a = frozenset([1, 2, 3, 4])
# can't be edited(immutable)







