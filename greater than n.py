'''
Write a Python program to find the list of words that are longer than n from a given list of words.
'''
str='this is python'
lst=[]
for a in str.split():
    if len(a)>=3:
        lst.append(a)
print(lst)