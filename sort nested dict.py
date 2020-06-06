'''
Write a Python program to sort a list of nested dictionaries.
'''
lst = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
lst.sort(key=lambda e:e['key']['subkey'],reverse=False)
print(lst)
