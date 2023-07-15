from collections import Counter, namedtuple, defaultdict, deque

# counter

a = "aaabbbbbcccccc"
mycounter = Counter(a)
print(mycounter)
print(mycounter.items())
print(mycounter.most_common((1)))
print(mycounter.most_common((1))[0][0])
print(list(mycounter.elements()))

# tuple

point =namedtuple("point", "x,y")
pt =point(1, -4)
print(pt.x, pt.y)


# default dictionary

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque - double ended que


de = deque()

de.append(1)
de.append(2)

de.appendleft(3)
print(de)

de.popleft()
print(de)

# de.clear()
# print(de)

de.extendleft(4)
print(de)