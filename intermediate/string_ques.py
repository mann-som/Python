
s = input()

# print(s.isalnum())
is_alnum = False
is_alphabet = False
is_digit = False
is_lower = False
is_upper = False
for i in range(len(s)):
    if s[i].isalnum():
        is_alnum = True

    if s[i].isalpha():
        is_alphabet = True

    if s[i].isdigit():
        is_digit = True

    if s[i].islower():
        is_lower = True

    if s[i].isupper():
        is_upper = True

print(is_alnum)
print(is_alphabet)
print(is_digit)
print(is_lower)
print(is_upper)
