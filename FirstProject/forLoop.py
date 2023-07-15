# for letter in "mann":
#     print(letter)
#
# nums = [0, 1, 3, 5, 6, 8]
# for num in nums:
#     print(num)
#
# for num in range(2, 8):
#     print(num)
#
# friends = ["jim", "karen", "kevin"]
#
# for n in range(len(friends)):
#     print(friends[n])



def power(base, pow):
    result = 1
    for n in range(pow):
        result = result * base
    return result

print(power(100,100))