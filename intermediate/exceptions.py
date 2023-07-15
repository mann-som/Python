# x = -5
# if x < 0:
#     raise Exception("x should be positive")

# assert (x>=5), 'X is not positive'

try:
    a = 5/0
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything's fine")
finally:
    print('cleaning up...')


class ValueTooHighError(Exception):
    def __init__(self, value, messaage):
        self.value = value
        self.message = messaage

class ValueTooSmallError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message

def test_case(x):
    if x > 100:
        raise ValueTooHighError('value is too high', x)
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

try:
    test_case(150)
except ValueTooHighError as e:
    print(e.value, e.message)
except ValueTooSmallError as e:
    print(e.value, e.message)