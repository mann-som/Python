from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
a = [1, 2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

a1 = [1, 2, 3]
perm = permutations(a1)
print(list(perm))

a2 = [1, 2, 5, 3, 4]
comb = combinations(a2, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a2, 2)
print(list(comb_wr))

acc = accumulate(a2, func=max)
print(list(acc))

def smaller_than_3(x):
    return x < 3

group_ojb = groupby(a2, key=smaller_than_3)
for key, value in group_ojb:
    print(key, list(value))

persons = [
    {'name': 'tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28}
]

group_ojb1 = groupby(persons, key=lambda x: x['age'])
for key, value in group_ojb1:
    print(key, list(value))











