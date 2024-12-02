#write a program without using eval() to get a input value
l = input("enter the list : ")

s = int(l)

print(l[0])
print(type(s))

print(type(l[0]))

#print a integers list to divisible with 7 but not with 5 from 100 to 200

value = []

for ss in range(100, 201):
    if ss % 7 == 0 and ss % 5 != 0:
        value.append(ss)

print(value)

#python program to add multiple in elements to the list.
 
a = [0,1, 2, 3]
 
elements_to_add = [4, 5, 6,7]
for element in elements_to_add:
    a.append(element)
 
print(a)
 