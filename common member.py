'''
Write a Python function that takes two lists and returns True if they have at least one common member.
'''
lst1=[1,2,3,4,5]
lst2=[1,6,7,8,9]
count=0
for a in lst1:
    for b in lst2:
        if a==b:
            count+=1
if count!=0:
    print(True)