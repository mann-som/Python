
mydict = {"name": "Mann", "age": 20, "City": "Delhi"}
mydict2 = dict(name= "Taneesha", age= 20, gender= "female")

print(mydict)

try:
    print(mydict["lastname"])
except:
    print("error")

for key in mydict.keys():
    print(key)

mydict.update(mydict2)
print(mydict)


mytuple = (2 ,5)
mydict3 = {mytuple: 7}

print(mydict3)