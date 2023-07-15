
# boolean

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are a short female")


if is_male and is_tall:
    print("You are a male or tall or both")
else:
    print("You are a short female")


if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are a short female")


# comparator


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1;
    elif num2 >= num1 and num2 >= num3:
        return num2;
    else:
        return num3;
result = max_num(5,7,2)
print("Maximum number is " + str(result))