# Write a program to create a set.
a = set([1,2,3,4,6])
print("set is use to create a set :",a)
s = {23,45,77,88}
print("set is use to create curly braces :", s) 

# Write program to iterate over sets.
a = {1,2,3,4,5}
for i in a :
    print("program to iterate over set :",i)

# Write a Python program to add member to a set.
a = {"vamsi","pavan","praveen"}
a.add("deva")
print("add members to a set :",a)

# Write a Python program to remove item from a given set.
a = {"vamsi","pavan","praveen","deva"}
a.remove("vamsi")
print("after remove item from given set :",a)

# Write a python program to create a intersection of set
a = {1,2,3,4}
b = {5,6,3,4}
s = a.intersection(b)
print("create a intersection of set :",s)

# Write a python program to createa unionof set ?
a = {1,2,3,4}
b = {5,6,3,4}
print("create union of set :",a.union(b))

# Write a python program to create set differance ?
a = {1,2,3,4}
b = {5,6,3,4}
print("create a set difference :",a.difference(b))

# Write a python program to create a symmetric defferance ?
a = {1,2,3,4}
b = {5,6,3,4}
print("create a symmetic defferance :",a.symmetric_difference(b))

# write a python program to find max and min values in a set?
a = {23,34,5,56,57}
s = max(a)
print("find max value of set :",s)
s = min(a)
print("find min value of set :",s)

# Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
a = {1,2,3,4}
b = {5,6,3,4}
a.difference_update(b)
print("update set :",a)

# Write a Python program to remove items 10, 20, 30 from the following set at once.?
a = {10,20,30,40,50,60}
remove_elements = {10,20,30}
for i in remove_elements :
 a.remove(i)
print("remove items of 10,20,30 in set :",a)

# Check if two sets have any elements in common. If yes, display the common elements?
a = {1,2,3,4,7}
s = {2,3,6,9,8}
common_elements = a.intersection(s)
if common_elements :
 print("print the common elements :",common_elements)
else:
  print("no common elements")
 
# Update set1 by adding items from set2, except common items?
set1 = {1,2,3,4,5,7}
set2 = {2,3,5,6,9,8}
set1.update(set2)
print("Updateing and adding items except common items :",set1)

# Remove items from set1 that are not common to both set1 and set2?
set1 = {1,2,3,4,5,7}
set2 = {2,3,5,6,9,8}
set1.intersection_update(set2)
print("remove elements that are not common in both sets :",set1)

# Write a python program to  add a key to a dictionary ?

a = {"name":"pavan","age":34}
a["percentage"] = 87.5556
print("add a key indictionary :",a)

# Write a python program to check weather the given value is present in the dictionary or not ?
a = {"name":"pavan","age":34,"percentage": 87.5556}
if "name" in a :
  print("the given value is present in the dictionary")
else :
  print("the given value is not present in the dictionary")

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
a = {i: i**2 for i in range(1,16)}
print(a)

# Write a python program to create a dictionary from the string ?
string = "{'A':13, 'B':14, 'C':15}"
Dict = eval(string)
print(Dict)
print(Dict['A'])
print(Dict['C'])

# Write a python program to combine two dictionaries by adding values of common keys ?

s = {'a': 10, 'b': 20, 'c': 30}
r = {'a': 5, 'b': 15, 'd': 25}
a = {}
for key in s:
    a[key] = s[key]
for key in r:
    if key in a:
      a[key] += r[key]
    else:
        a[key] = r[key]
print("Combined Dictionary:",a)

# Write a python program to merge two python dictionaries ?
dict1 = {1,2,3,4,5,7}
dict2 = {2,3,5,6,9,8}
dict1.update(dict2)
print("merge two dictionaries :",dict1)

# Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
input_string = 'skywavessoftwares'
count_dict = {}
for char in input_string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
print("Character count dictionary:", count_dict)
