'''
Write a Python program to get the frequency of the elements in a list.
'''
lst=[9,8,7,1,2,3,4,4,4,5,9,5]
import collections
c=collections.Counter(lst)
print(c)