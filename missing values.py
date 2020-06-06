'''
Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
'''
lst=[1,2,3,4,5]
lst1=[4,5,6,1,2,7,8]
c=len(lst)
for i in lst:
    while c!=0:
            if i not in lst1:
                print(i,end='')
            c-=1
print(lst1[c:])