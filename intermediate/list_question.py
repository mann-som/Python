
N = int(input())
arr = []

for i in range(N):
    query = input().split()
    # num1 = num
    # print(query, num, ind[0])
    if query[0] == "insert":
        arr.insert(int(query[1]), int(query[2]))
    elif query[0] == "print":
        print(arr)
    elif query[0] == "append":
        arr.append(int(query[1]))
    elif query[0] == "remove":
        arr.remove(int(query[1]))
    elif query[0] == "sort":
        arr.sort()
    elif query[0] == "pop":
        arr.pop()
    elif query[0] == "reverse":
        arr.reverse()
    else:
        print("WRONG COMMAND")





