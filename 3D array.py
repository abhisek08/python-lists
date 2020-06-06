'''
Write a Python program to generate a 3*4*6 3D array whose each element is *.
'''
lst=[]
for i in range(6):
    for j in range(4):
        for k in range(3):
            lst.append('*')
            print([lst])