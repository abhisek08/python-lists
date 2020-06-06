'''
Write a Python program to convert a list of characters into a string.
'''
lst=['a','b','h','i']
import functools
c=functools.reduce(lambda a,b:a+b,lst)
print(c)