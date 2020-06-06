'''
Write a Python program to remove duplicates from a list.
'''
lst=[1,1,1,2,2,2,3,3,4,4,5]
print(lst)
s=set(lst)
lst=list(s)
print(lst)