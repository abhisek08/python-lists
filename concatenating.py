'''
Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
lst=['p','q']
n=5
c=1
lst1=[]
while c<=5:
    lst1.append(lst[0]+str(c))
    lst1.append(lst[1] +str(c))
    c+=1
print(lst1)
