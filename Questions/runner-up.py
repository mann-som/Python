
students = [
    ["chi", 20],
    ["Mark", 20],
    ["beta", 50],
    ["alpha", 50],
    ["sam", 60],
    ["alex", 90],
]

max_num = second_max = 0


for ele in students:
    if ele[1] < max_num:
        second_max = max_num
        max_num = ele[1]
    elif ele[1] < second_max:
        second_max = ele[1]

print(second_max)
