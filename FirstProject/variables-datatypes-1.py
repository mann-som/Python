# importing module files

from math import*



character_name = "john"
character_age = "35"
print("There was once a man named " + character_name + ",")
print("He was " + character_age + " year old")


# strings


print("Mann\nsom")
phrase = "Mann Som"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("n"))
print(phrase.replace("Som","kumar"))


#numbers


print(2+5.6)
num = 5
num2 = -5
print(num)
print(str(num))
print(str(num) + " is my favourite number")
print(abs(num2))
print(pow(5,2))
print(max(5,2), min(5,2))
print(round(3.2), round(3.8))
print(floor(3.7), ceil(3.2))
print(sqrt(36))


# getting input from user


# name = input("Hey, what's your name: ")
# age = input("what's your age: ")
# print("hey, it's " + name)
# print("he is " + age + " years old")

# num1 = input("enter the first number: ")
# num2 = input("enter the second number: ")
# result = int(num1) + int(num2)
# print(str(num1) + "+" + str(num2) + "=" + str(result))
# print(result)


# madlibs game

color = input("enter a color: ")
plural_noun = input("enter a plural noun: ")
celeb = input("enter a celebrity name: ")

print("roses are " + color)
print(plural_noun + " are blue")
print("i love " + celeb)