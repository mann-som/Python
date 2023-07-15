
n = int(input())
student_marks = {}
if 1 <= n <= 10:
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


for key in student_marks.keys():
    if key == query_name:
        marks_list = student_marks[key]


average = (marks_list[0] + marks_list[1] + marks_list[2])/3
final = "{:.2f}".format(average)
print(marks_list)
print(average)
print(final)

