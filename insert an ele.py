'''
Write a Python program to insert an element before each element of a list.
'''
color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for elt in color for v in ('c', elt)]
print("Original List: ",color)

l=[1,2,3]
for i in l:
    for j in (0,i):
        print(j,end='')