nums = [0, 1, 2, 3, 4, 5, 6, 7]
friends2 = ["taneesha", "ritek", "khalid", "laksh", "Manav", "Manav"]
friends = ["taneesha", "ritek", "khalid", "laksh", "Manav", "Manav"]
friends3 = friends.copy()
print(friends3)
friends[3] = "chutiya"
friends.extend(nums)
friends.append("Mann")
friends.insert(1, "Lipi")
friends.remove("Mann")
# friends.clear()
print(friends.count("Manav"))
print(friends.index("ritek"))
friends.pop()
print(friends)
print(friends[2])
print(friends[-2])
print(friends[1:3])
nums.sort()
print(nums)
friends2.sort()
print(friends2)

#Tuples

coordinates = [(4,5),(2,3)]
print(coordinates)