'''
 Write a Python program to convert a list of multiple integers into a single integer.
'''
lst=[11,22,33]
str1=''
for i in lst:
    str1=str1+str(i)
print(int(str1))