import logging
# from collections import Counter

logging.basicConfig(filename='test.log',level= logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


num1 = 20
num2 = 10

add_result = add(num1, num2)
logging.debug(add_result)

sub_result = subtract(num1, num2)
logging.debug(sub_result)

mul_result = multiply(num1, num2)
logging.debug(mul_result)

div_result = divide(num1, num2)
logging.debug(div_result)

