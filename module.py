#!usr/bin/env python3

"""module.py - an example of python module """

__counter = 0

def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prod1(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("Hi I really like to be a module, but I can help you with your test")
    l = [i + 1 for i in range (5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)


# module.py

#!/usr/bin/env python3 

""" module.py - an example of Python module """

"""__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prodl(list):
    global __counter    
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)"""
