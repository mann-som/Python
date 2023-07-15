import random


a = random.random()
print(a)
b = random.uniform(1, 10)
print(b)
c = random.randint(1, 10)
print(c)
mylist = list("ABCDEF")
d = random.choice(mylist)
print(d)
e = random.sample(mylist, 3)
print(e)

