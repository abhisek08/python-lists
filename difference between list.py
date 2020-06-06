'''
Write a Python program to get the difference between the two lists.
'''
lst=[1,2,3,4,5]
lst1=[6,7,8,9,10]
diff=[]
n=0
while n<len(lst1):
    diff.append(lst1[n]-lst[n])
    n+=1
print(diff)