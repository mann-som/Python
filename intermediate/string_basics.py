from timeit import default_timer as timer


mystring = "Hello world"

print(mystring[::1], mystring[::2], mystring[::-1])

greeting = "    Hello    "
name = "Max"

print(greeting + name)

for i in greeting:
    print(i)



greeting = greeting.strip()
print(greeting)

print(mystring.startswith("H"))


mylist = mystring.split()
# default argument is space
print(mylist)

new_string = ''.join(mylist)
print(new_string)

# bad approach
teststring = ['a'] * 100000
start = timer()
my_string = ""
for i in teststring:
    my_string =+ 1
stop = timer()
print(stop-start)

# better aproach
start = timer()
my_string = ' '.join(teststring)
stop = timer()
print(stop-start)

# formating a string
# %, format(), f-string

var = 3.12345566
var1 = 6
varstring1 = "The variable is %d" %var
varstring = "The variable is {:.2f} and {}".format(var, var1)
varstring2 = f"The variable is {var} and {var1}"
print(varstring)
print(varstring1)
print(varstring2)














