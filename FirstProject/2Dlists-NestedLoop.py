
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


print(number_grid[2][2])


for row in number_grid:
    for col in row:
        print(col)

# translator
# every vowel is converted to M & m

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "M"
            else:
                translation = translation + "m "
        else:
            translation = translation + letter

    return translation

print(translator(input("Enter a phrase: ")))