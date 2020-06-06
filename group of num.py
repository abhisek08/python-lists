'''
Write a Python program to generate groups of five consecutive numbers in a list
'''
lst=[]
lst1=[]
for i in range(3):
    lst.append(i)
for i in range(5):
    lst1.append(lst)
print(lst1)