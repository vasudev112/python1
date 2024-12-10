# 1.Write a function that takes a tuple and an index as inputs and returns the element at the given index. Handle the case where the index is out of bounds.

def n(input_tuple, index):
    try:
        return input_tuple[index]
    except IndexError:
        return "Index is out of bounds"
 
n1 = (10, 20, 30, 40)
 
print(n(n1, 2))  
print(n(n1, 5))

# 2.Write a function to concatenate two tuples into one.
a = (1,2,3,4)
t = ("d","s","d","f")
print(type(t))
print("concatenate two tuple in one :",a+t)

# 3.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.
t = (1,2,3,4,2,3,2,4,2)
print(type(t))
print("number of times 2 return :", t.count(2))

# 4.Write a function that calculates the length of a tuple without using the built-in `len()` function.
s =(1,2,3,4)
print(type(s))
count = 0
for _ in s:
        count+=1
        
print("length of tuple without using len() :",count)

# 5.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.
a = (1,2,3,4,5)
print(type(a))
print("tuple element in reverse order :",a[::-1])

# 6.Write a function to concatenate two tuples into one.
def concatenate_tuples(s, a):
    return a + s
s =(1,2,3,43)
a = (33,44,65)
print(type(s))
result = concatenate_tuples(a, s)
print(result) 
 
# 7.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.
r = (1,2,3,5,6,7,5,2,5,6,5)
print(r)
print(type(r))
x = [i for i in r if i == 5]
print("the number of times 5 returns", len(x))

# 8.Write a function that calculates the length of a tuple without using the built-in `len()` function.
s =(1, 2, 3, 4, 5)
print(type(s))
length = sum(1 for _ in s)

print("Length of the list:", length)

# 9.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.
def Reverse(c):
	new_tup = ()
	for k in reversed(c):
		new_tup = new_tup + (k,)
	print("tuple after reverse : ",new_tup)

c = (10, 11, 12, 13, 14, 15)
Reverse(c)
print("tuple before reverse :",c)

# 10.Write a function that checks if a given element exists in a tuple. Return `True` if it exists, otherwise return `False`.

t = (1,2,3,4,5)
print(t)
print(type(t))
if 4 in t:
       print("the given element exists in tuple  :",True)
else :
        print("the given element exists in tuple  :",False)

# 11.Write a function that takes two tuples and returns a tuple containing the common elements.
a = (1,2,3,4,5)
d = (4,5,6,7)
print(a)
print(type(a))

common = list(set(a)&set(d))
print("commen elements in two tuples: ",common)     

# 12.Write a function to unpack nested tuples and flatten them into a single tuple.  
# example 
# Input: ((1, 2), (3, 4), 5)
# output : (1,2,3,4,5)
def flatten_tuple(tup):
    result = []
    for item in tup:
        if isinstance(item, tuple):
            result.extend(flatten_tuple(item))
        else:
            result.append(item)
    return tuple(result)

nested_tuple = ((1, 2), (3, 4), 5)
print(flatten_tuple(nested_tuple))
