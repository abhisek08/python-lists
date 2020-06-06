'''
Write a Python program to generate and print a list except for the first 5 elements,
where the values are square of numbers between 1 and 30 (both included).
'''
c=range(1,31)
lst=[]
for i in c:
    lst.append(i**2)
print(lst[5:])