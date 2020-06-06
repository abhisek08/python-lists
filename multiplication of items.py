'''
Write a Python program to multiplies all the items in a list.
'''
lst=[4,3,6,98,2,1]
import functools
a=functools.reduce(lambda a,b:a*b,lst)
print(a)
