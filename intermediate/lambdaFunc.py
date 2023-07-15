
# lambda argument: expression
# map(func, seq)
# filter(func, seq)
# reduce(func, seq)

from functools import reduce

add10 = lambda x: x +10

print(add10(5))

mult = lambda x,y: x*y
print(mult(2,3))

point2d = [(1,2), (15, 1), (5, -1), (10, 4)]
print(point2d)

point2d_sorted = sorted(point2d)
print(point2d_sorted)

point2d_sorted1 = sorted(point2d, key=lambda x: x[1])
print(point2d_sorted1)

point2d1 = [(1,2), (15, 1), (5, -1), (10, 4)]
print(point2d1)

point2d_sorted2 = sorted(point2d1)
print(point2d_sorted)

point2d_sorted3 = sorted(point2d1, key=lambda x: x[0] + x[1])
print(point2d_sorted1)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

d = filter(lambda x: x%2==0, a)
print(list(d))

e = [x for x in a if x%2==0]
print(e)

product_a = reduce(lambda x,y: x*y, a)
print(product_a)

















