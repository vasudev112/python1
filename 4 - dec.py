# Basic List Operations:
# create a list of 5 integers and print sum of all elements in list
print("sum of 5 integers")
a = [1,2,3,4,5]
print("orginal list :",a)
a = sum(a)
print("use sum list :",a)
# Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.
print("print second and fourth elements")
s = ["apple","banana","grapes","orange","mango"]
print("orginal list :",s)
print("print second element :",s[1])
print("print fourth element :",s[4])

# Adding and Removing Elements:
# Write a Python program that initializes a list with some numbers and:
print("Write a Python program that initializes a list with some numbers and add and remove")
print('adding elements')
a = []
print("orginal list :",a)
a = [1,2,3,4]
print("after adding :",a)
print("removing elements")
a.remove(2)
print("after removing :",a)

# Adds a new number to the list using the append() method.
print("add a new element using append")
a = []
for i in range(100): 
  a.append(0)
print(len(a))

# Inserts a number at the second position using insert().
print("insert a number in second position using insert")
a = [1,2,3,4,5]
print("orginal :",a)
a.insert(1,22)
print("after insert :",a)

# Extends the list with another list of numbers.
print("Extends the list with another list of numbers")
a = [10,20,30]
b = [50,60]
print("orginal list :",a ,b)
a.extend(b)
print("using extends list :",a)

# Remove all occurrences of the number 3 from a list of integers.
print("remove all number 3 in list")
a = (1,2,3,4,6,7,3,8,9,)
print("orginal list :",a)
a = [i for i in a if i != 3]
print("remove 3 :",a)

# Write a Python program to remove the last element of a list using pop() and print the updated list.
print(" remove the last element of a list using pop() and print")
s = [ 1,2,3,4]
print("orginal list",s)
s.pop(-1)
print("using pop :",s)

# Sorting and Reversing Lists:
# Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().
print(" sort a list of 10 random integers in ascending and descending order using sort() and reverse()")
a = [1,2,3,5,7,-1,-2,8,0]
print("orginal value :" ,a)
a.sort()
print("ascending order :",a)
a.reverse()
print("descending order :",a)

# Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.
print("reverse the order of elements using both reverse() and slicing [::-1]")
b = [1,2,3,4]
print("orginal list :",b)
b.reverse()  
print("using reverse :",b)
a = b[::-1]
print("usung slicing :",b)

# Aliasing and Cloning:
'''1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes.
Then, create a copy of the original list and show that modifying the copy does not affect the original list.'''
print("create a list and copy and modify")
orginal_list = [  1,2,3,4,5  ]
second_list = orginal_list
orginal_list.append(6)
print("orginal_list :",orginal_list)
print("second_list :",second_list)
modifyed_list = second_list.copy()
modifyed_list.append(7)
print("orginal_list after modifying :",orginal_list)
print("modifyed_list :",modifyed_list)
 
# Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.

# Original list
original_list = [1, 2, 3, 4, 5]
alias_list = original_list
cloned_list = original_list.copy()
alias_list.append(6)
cloned_list.append(7)
print("Original list after modification via alias:", original_list)
print("Alias list after modification:", alias_list)
print("Cloned list after modification:", cloned_list)

# Mathematical Operations:
# Create two lists of numbers and use the + operator to concatenate them.Then use the * operator to repeat the elements of one list 3times

print("create 2 lists using +,* operators")
a = ("welcome ")
b = (" my program")
s = a+b
print("using + operator:", s)
s = a*3
print("using * operator :", s)

# Given a list of numbers write a Python program to create a new list where each element is doubled  each element is multiplied by 2)
s = [1,2,3,4,5]
print("orginal list :",)
double = [x * 2 for x in s]
print("after doubled and %2 :",double)

# Membership Operators:
# Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
print("check the position of given number")
a = [1,2,3,4,5,6]
s = 5
if s in a :
  position =a.index(s)
  print("element", (s))
  print("position" ,(position))
else : 
 print("element is not found")

# Given a list of student names, check if "John" and "Sara" are in the list using the in operator.
name = ["raju","john","deva","sara","pinky "]
if "john" in name :
  print("john is in name.")
else :
  print ("john is not in name")
if "sara" in name :
  print("sara is in name.")
else :
  print("sara is not in name.")

# Nested Lists:
# Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
a = [[2,3,4],[3,4,5],[7,8,9]]
print("3*3 matrix :")
for row in a :
 print(row)
element = a[1][2] 
print("elements" ,element)
# Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
student_grades =[["sai", 85],["ravi", 95],["pavan", 97],["deva", 85]]
for student in student_grades :
  name = student[0]
  grade = student[1] 
  print(f"student_grades: {name} grades  :{grade}.")

# Advanced Challenges:
# 1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#Another containing only the odd numbers
#one containing only the even numbers.

number = (list(range (1 ,20)))
even_number =[num for num in number if num % 2 == 0 ]
odd_number =[num for num in number if num %2 != 0 ]
print("even numbers :",even_number)
print("odd numbers :",odd_number)

# Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
a = [1,3,2,3,2,7,5,5,6,6,7]
print("orginal :",a)
b = (list(set(a)))
print("after remove duplicate :",b)

#  Given a list of tuples representing (name, age), sort the list by age in ascending order.
people = [("vijay", 30), ("deva", 25), ("pavan", 35), ("vamsi", 20)]
sorted_people = sorted(people, key=lambda person: person[1])
print("Sorted list by age:", sorted_people)
