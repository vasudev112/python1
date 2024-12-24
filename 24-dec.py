#python program to find index values of a mid charector	
a = input("enter the string:" )
x = len(a)
y = x//2
print("middle value:",a[y])	
	
#print a integers list to divisible with 7 but not with 5 from 100 to 200

value = []

for ss in range(1, 101):
    if ss % 7 == 0 and ss % 5 != 0:
        value.append(ss)

print(value)

#pop remove returns the last  element
l = [23,54,7,97,88,79,11]
pop = l.pop()
print(pop)
print(l)
#remove specified elements from the list
l = [20,30,40,50,90,100]
rl = l.remove(90)
print(rl)
print(l)

# 4.Write a function that calculates the length of a tuple without using the built-in `len()` function.
s =(5,7,8,3)
print(type(s))
count = 0
for _ in s:
        count+=1
        
print("length of tuple without using len() :",count)

# Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
input_string = 'wellcome'
count_dict = {}
for char in input_string:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
print("Character count dictionary:", count_dict)

# union()
a = {10,20,30,40,50,60}
s = {40,50,70,80}
print(a.union(s))

# intersection
a = {10,20,30,40,50,60}
s = {50,60,70,80}
print(a.intersection(s))
