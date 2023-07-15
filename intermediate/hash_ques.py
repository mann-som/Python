from builtins import hash


n = int(input())
integer_list = map(int, input().split())

my_tuple = tuple(integer_list)

my_hash = hash(my_tuple)


print(my_hash)