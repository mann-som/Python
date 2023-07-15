import functools


def repeat(num_times):
    def deco_repeats(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco_repeats


@repeat(num_times=5)
def greet(name):
    print(f"Hello {name}")


greet("mann")