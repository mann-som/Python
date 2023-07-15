import functools


def start_end_deco(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper

# @start_end_deco
# def print_name():
#     print("Mann")

# print_name()

# print_name1 = start_end_deco(print_name)

# print_name()

@start_end_deco
def add5(x):
    return x + 5

result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)

