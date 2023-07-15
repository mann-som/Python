
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#

# buiding guessing game

word = "code"
guess = ""
i = 0;
gcount = False

while guess != word and not(gcount):
    if i < 3:
        guess = input("Enter your guess: ")
        i += 1
    else:
        gcount = True

if gcount:
    print("OOH YOU LOSE!")
else:
    print("YOU GOT IT!")