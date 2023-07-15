

students = [
    ["chi", 20],
    ["Mark", 20],
    ["beta", 50],
    ["alpha", 50],
    ["sam", 60],
    ["alex", 90],
]

print(students[1][1])


slg = lg = float('inf')

for s in students:
    if s[1] < lg:
        slg = lg
        lg = s[1]
    elif s[1] == lg:
        continue
    elif s[1] < slg:
        slg = s[1]

print(lg, slg)
