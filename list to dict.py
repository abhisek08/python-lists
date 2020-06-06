'''
Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},
 {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
'''
l=["Black", "Red", "Maroon", "Yellow"]
m=["#000000", "#FF0000", "#800000", "#FFFF00"]
dict={}
lst=[]
for i in range(4):
    j={'color':l[i],'code':m[i]}
    lst.append(j)
print(lst)
