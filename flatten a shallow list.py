'''
Write a Python program to flatten a shallow list.
'''
lst=[[1,2,3],[4,5,6],[7,8,9,10]]
lst1=[]
for i in lst:
    for j in i:
        lst1.append(j)
print(lst1)
import itertools
c=tuple(itertools.chain(*lst))
print(c)