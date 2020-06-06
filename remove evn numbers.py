'''
Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''
lst=[2,1,5,4,6,7,84,5,6,77,96,14,32,23,56,233,12,54,59,71,24]
lst1=[]
for i in lst:
    if i%2!=0:
        lst1.append(i)
print(lst1)
